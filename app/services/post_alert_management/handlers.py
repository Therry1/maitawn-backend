"""
Handlers pour le service Post Alert Management
Contient la logique métier du service
"""
import asyncio
from datetime import datetime
import math
from typing import List, Optional
from uuid import UUID, uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status

from google.cloud.firestore_v1.base_query import FieldFilter
from app.common.upload_file import save_uploaded_file
from app.services.post_alert_management.constants import ValidationState
from app.services.post_alert_management.schemas import PostAlertResponse, PostAlertSchemaStore

# fonction de haversine pour calculer la distnce entre deux point A et B
async def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Rayon Terre en km

    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)

    a = (
        math.sin(d_lat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(d_lon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c  # distance en km

# fonction permettant de faire l'upload des fichiers
async def upload_files ():
    
    return 'ok'

# fonction permettant de faire une alert
async def make_post_alert (db , payload , attachment):
    #try:
    payload = payload.model_dump()
    # verifier si l'on dispose des institutions pour le traitement de la catégorie envoyé
    institution_category_docs = await asyncio.to_thread(
        lambda: list(
            db.collection('institution_categories')
            .where(
                filter=FieldFilter(
                    "id",
                    "==",
                    str(payload["post_category_id"])
                )
            )
            .stream()
        )
    )

    if len(institution_category_docs) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Le type de votre post n'est pas pris en charge"
        )

    # recherche de toutes les institutions qui on la categorie renseigné
    institutions = await asyncio.to_thread(
        lambda: list(
            db.collection('institutions').where(
                filter=FieldFilter(
                    "category_id",
                    "==",
                    str(payload["post_category_id"])
                )
            ).stream()
        )
    )
    
    # verifier que le tableau généré n'est pas vide
    if len(institutions) <= 0:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"le systeme ne dispose pas d'institution capable de traiter votre post"
        )
    # stokage des longitudes et latitudes pour la recherche de 'institution de reference
    post_longitude = payload['longitude']
    post_latitude = payload['latitude']
    
    #print (f"aaaaaaaaaa: {str(institutions[0].to_dict()['location'])}")
    ref_longitude = (institutions[0].to_dict())['location']['longitude']
    ref_latitude = (institutions[0].to_dict())['location']['latitude']
    # prise de la premiere institution comme reférence
    min_distance = await haversine_distance(
        post_latitude , post_longitude,  ref_latitude , ref_longitude
    )
    min_location = institutions[0].to_dict()
    for institution in institutions:
        institution = institution.to_dict()
        institution_location = institution['location']
        
        if not institution_location:
            continue
        
        location_distance = await haversine_distance(
            post_latitude , post_longitude,  institution_location['latitude'] , institution_location['longitude']
        )
        
        if location_distance < min_distance:
            min_distance = location_distance
            min_location = institution
            
    # upload du fichier attaché au post
    filename , file_path = await save_uploaded_file(attachment , min_location['id'])
    
    
    # envois du post avec les donnée retrouvé en fonction de a localisation minimal
    post_alert_id = uuid4()
    institution_ids = []
    institution_ids.append(str(min_location['id']))
    post_data = PostAlertSchemaStore(
        id = str(post_alert_id),
        post_category_id = str(payload['post_category_id']),
        institution_ids = institution_ids,
        location = {
            'longitude' : post_longitude,
            'latitude' : post_latitude,
        },
        file_name = filename,
        file_url = file_path,
        state = ValidationState.pending,
        created_at = datetime.utcnow()
    )
    
    post = await asyncio.to_thread(
        lambda: db.collection('post_alerts').document(str(post_alert_id)).set(
            post_data.model_dump()
        )
    )
        
    return payload
    # except Exception as exception:
    #     raise HTTPException(
    #         status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
    #         detail=f"{str(exception)}"
    #     )

# fonction permettant de lister les post d'alert en fontion de 'id de l'institution
async def list_post_by_institution_id(
    db,
    institution_id: UUID = None,
    category_id: UUID = None,
    state: ValidationState = None
):
    try:
        query = db.collection('post_alerts')

        if institution_id is not None:
            query = query.where(
                'institution_ids',
                'array_contains',
                str(institution_id)
            )

        if category_id is not None:
            query = query.where(
                'post_category_id',
                '==',
                str(category_id)
            )
            
        if state is not None:
            query = query.where(
                'state',
                '==',
                state
            )

        post_list_result = await asyncio.to_thread(
            lambda: list(query.stream())
        )

        post_list = []

        for doc in post_list_result:
            item = doc.to_dict()

            location = item.get('location', {})

            post_list.append(PostAlertResponse(
                post_category_id=item.get('post_category_id'),
                institution_id=item.get('institution_ids'),
                latitude=location.get('latitude'),
                longitude=location.get('longitude'),
                file_name=item.get('file_name'),
                file_url=item.get('file_url'),
                created_at=item.get('created_at'),
                state=item.get('state')
            ))

        return post_list

    except Exception as exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exception)
        )