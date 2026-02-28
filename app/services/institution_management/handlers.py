"""
Handlers pour le service Institution Management
Contient la logique métier du service
"""
import asyncio
from typing import List, Optional
from uuid import UUID, uuid4
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status

from app.services.institution_management.constants import IntitutionCat , ADAMAOUA_DATA
from app.services.institution_management.schemas import (
    InstitutionCategoryBase,
    InstitutionCreate,
    InstitutionResponse,
    InstitutionUpdate
)
# from app.common.models.InstitutionManagement import InstitutionManagement


async def clear_collection(db, collection_name: str):
    docs = await asyncio.to_thread(lambda: list(db.collection(collection_name).stream()))
    for doc in docs:
        # On passe une lambda qui appelle delete()
        await asyncio.to_thread(lambda d=doc: db.collection(collection_name).document(d.id).delete())
        
async def list_regions(db):
    try:
        docs = await asyncio.to_thread(
            lambda: list(db.collection("regions").stream())
        )

        regions = []
        for doc in docs:
            data = doc.to_dict()
            data["id"] = UUID(data["id"])
            regions.append(data)

        return regions

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def list_departments(db):
    try:
        docs = await asyncio.to_thread(
            lambda: list(db.collection("departements").stream())
        )
        departments = []
        for doc in docs:
            data = doc.to_dict()
            data["id"] = UUID(data["id"])
            data["region_id"] = UUID(data["region_id"])
            departments.append(data)

        return departments

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
async def list_arrondissements(db):
    try:
        docs = await asyncio.to_thread(
            lambda: list(db.collection("arrondissements").stream())
        )

        arrondissements = []
        for doc in docs:
            data = doc.to_dict()
            data["id"] = UUID(data["id"])
            data["departement_id"] = UUID(data["departement_id"])
            arrondissements.append(data)

        return arrondissements

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
async def init_locations(db):
    """
    Vide les collections région, département, arrondissement,
    puis remplit avec les données de la région Adamaoua.
    """
    # 1️⃣ Vider les collections
    for col in ["arrondissements", "departements", "regions"]:
        await clear_collection(db, col)

    # 2️⃣ Ajouter la région, départements et arrondissements
    for region_data in ADAMAOUA_DATA:
        region_id = str(uuid4())
        await asyncio.to_thread(
            db.collection("regions").document(str(region_id)).set,
            {
                "id": region_id,
                "name": region_data["region"]
            }
        )

        for dept in region_data["departements"]:
            dept_id = str(uuid4())
            await asyncio.to_thread(
                db.collection("departements").document(str(dept_id)).set,
                {
                    "id": dept_id,
                    "name": dept["name"],
                    "region_id": region_id
                }
            )

            for arr in dept["arrondissements"]:
                arr_id = str(uuid4())
                await asyncio.to_thread(
                    db.collection("arrondissements").document(str(arr_id)).set,
                    {
                        "id": arr_id,
                        "name": arr,
                        "departement_id": dept_id
                    }
                )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "Collections de localisation initialisées avec succès"}
    )

async def create_institution_categories(db):
    
    data = []
    institution_category1 = InstitutionCategoryBase(label= 'mairie' , code='MAIRIE', type= IntitutionCat.mairie)
    await asyncio.to_thread(
        db.collection("institution_categories")
        .document(str(institution_category1.id))
        .set,
        institution_category1.model_dump(mode = 'json')  # pydantic v2
    )
    data = data + [institution_category1]
    
    return JSONResponse(
        status_code= status.HTTP_201_CREATED,
        content={
            'message' : 'les catégories d\'institutions ont été créé avec success',
            'data' : str(data)
        }
    )

async def list_institution_categories(db):

    docs = await asyncio.to_thread(
        lambda: list(
            db.collection("institution_categories").stream()
        )
    )

    result = []

    for doc in docs:
        data = doc.to_dict()

        # On s'assure que l'id correspond à l'id du document
        data["id"] = doc.id

        result.append(data)

    return result

async def create_institution_management(
    payload: InstitutionCreate,
    db
):
    try:
        # On garde l'objet original
        institution_dict = payload.model_dump()

        # Conversion UUID -> str
        institution_dict["id"] = str(payload.id)
        institution_dict["region_id"] = str(payload.region_id)
        institution_dict["department_id"] = str(payload.department_id)
        institution_dict["arrondissement_id"] = str(payload.arrondissement_id)
        institution_dict["category_id"] = str(payload.category_id)

        # location est déjà converti par model_dump()
        # donc PAS besoin de refaire model_dump()

        await asyncio.to_thread(
            lambda: db.collection("institutions")
            .document(institution_dict["id"])
            .set(institution_dict)
        )

        return {
            "message": "Institution créée avec succès",
            "data": institution_dict
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erreur lors de la création de l'institution: {e}"
        )
        
async def list_institutions(db):
    try:
        docs = await asyncio.to_thread(
            lambda: list(db.collection("institutions").stream())
        )

        institutions = []

        for doc in docs:
            data = doc.to_dict()

            # Conversion des champs string -> UUID
            data["id"] = UUID(data["id"])
            data["region_id"] = UUID(data["region_id"])
            data["department_id"] = UUID(data["department_id"])
            data["arrondissement_id"] = UUID(data["arrondissement_id"])
            data["category_id"] = UUID(data["category_id"])

            institutions.append(data)

        return institutions

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erreur lors du listing des institutions: {e}"
        )
        
         

async def get_institution_by_id(db, institution_id: UUID):
    try:
        doc = await asyncio.to_thread(
            lambda: db.collection('institutions')
            .document(str(institution_id))   # 🔥 IMPORTANT
            .get()
        )

        if not doc.exists:
            raise HTTPException(
                status_code=404,
                detail=f"Aucune institution avec l'id {institution_id} trouvée"
            )

        data = doc.to_dict()
        data["id"] = UUID(data["id"])

        return data

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
        
async def get_institution_management_by_id(
    item_id: UUID,
    db: AsyncSession
) -> InstitutionResponse:
    """
    Récupérer un institution_management par son ID
    
    Args:
        item_id: ID de l'objet
        db: Session de base de données
    
    Returns:
        InstitutionManagementResponse: L'objet trouvé
    
    Raises:
        HTTPException: Si l'objet n'existe pas
    """
    # TODO: Implémenter la logique de récupération
    # item = await db.get(InstitutionManagement, item_id)
    # if not item:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f"InstitutionManagement not found"
    #     )
    # return item
    
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Cette fonctionnalité n'est pas encore implémentée"
    )


async def get_all_institution_management(
    db: AsyncSession,
    skip: int = 0,
    limit: int = 100
) -> List[InstitutionResponse]:
    """
    Récupérer tous les institution_management
    
    Args:
        db: Session de base de données
        skip: Nombre d'éléments à sauter
        limit: Nombre maximum d'éléments à retourner
    
    Returns:
        List[InstitutionManagementResponse]: Liste des objets
    """
    # TODO: Implémenter la logique de récupération
    # stmt = select(InstitutionManagement).offset(skip).limit(limit)
    # result = await db.execute(stmt)
    # items = result.scalars().all()
    # return items
    
    return []


async def update_institution_management(
    item_id: UUID,
    data: InstitutionUpdate,
    db: AsyncSession
) -> InstitutionResponse:
    """
    Mettre à jour un institution_management
    
    Args:
        item_id: ID de l'objet
        data: Données de mise à jour
        db: Session de base de données
    
    Returns:
        InstitutionManagementResponse: L'objet mis à jour
    
    Raises:
        HTTPException: Si l'objet n'existe pas
    """
    # TODO: Implémenter la logique de mise à jour
    # item = await db.get(InstitutionManagement, item_id)
    # if not item:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f"InstitutionManagement not found"
    #     )
    # 
    # for key, value in data.model_dump(exclude_unset=True).items():
    #     setattr(item, key, value)
    # 
    # await db.commit()
    # await db.refresh(item)
    # return item
    
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Cette fonctionnalité n'est pas encore implémentée"
    )


async def delete_institution_management(
    item_id: UUID,
    db: AsyncSession
) -> dict:
    """
    Supprimer un institution_management
    
    Args:
        item_id: ID de l'objet
        db: Session de base de données
    
    Returns:
        dict: Message de confirmation
    
    Raises:
        HTTPException: Si l'objet n'existe pas
    """
    # TODO: Implémenter la logique de suppression
    # item = await db.get(InstitutionManagement, item_id)
    # if not item:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f"InstitutionManagement not found"
    #     )
    # 
    # await db.delete(item)
    # await db.commit()
    # return {"message": f"InstitutionManagement deleted successfully"}
    
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Cette fonctionnalité n'est pas encore implémentée"
    )
