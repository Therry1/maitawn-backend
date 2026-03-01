"""
Routes pour le service Post Alert Management
"""

from typing import Annotated, List
from uuid import UUID
from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database import get_db
from app.services.post_alert_management.constants import ValidationState
from firebase import get_firebase_db
from app.services.post_alert_management.schemas import (
    PostAlertBase,
    PostAlertForm,
    PostAlertResponse
)
from app.services.post_alert_management.handlers import (
    list_post_by_institution_id,
    make_post_alert
)

db = get_firebase_db()

router = APIRouter(
    prefix="/post-alert-management",
    tags=["Post Alert Management"]
)


from fastapi import Form, UploadFile, File
from uuid import UUID

@router.post(
    '/make-post-alert',
    status_code=status.HTTP_201_CREATED,
    summary="Route permettant de faire un post"
)
async def make_post_alert_path(
    form_data: Annotated[PostAlertForm, Depends()]
):
    dict_data = {
        "post_category_id"  : form_data.post_category_id,
        "latitude"          : form_data.latitude,
        "longitude"         : form_data.longitude,
    }
    payload = PostAlertBase(**dict_data)
    return await make_post_alert(db, payload, form_data.attachment)

@router.get(
    '/list-post-by-institution-id',
    response_model=List[PostAlertResponse],
    status_code=status.HTTP_200_OK,
    summary= "route servant à lister les post d'alert en fonction de l'istitution"
)
async def list_post_by_institution_id_path(
    institution_id: UUID = Query(None),
    category_id : UUID = Query(None),
    state: ValidationState = Query(None)
):
    return await list_post_by_institution_id(db , institution_id , category_id , state)
