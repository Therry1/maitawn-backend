"""
Routes pour le service Street Light Management
"""

from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database import get_db
from app.common.auth import get_current_user
from app.services.street_light_management.schemas import (
    StreetLightManagementCreate,
    StreetLightManagementUpdate,
    StreetLightManagementResponse
)
from app.services.street_light_management.handlers import (
    create_street_light_management,
    get_street_light_management_by_id,
    get_all_street_light_management,
    update_street_light_management,
    delete_street_light_management
)

router = APIRouter(
    prefix="/street_light_management",
    tags=["Street Light Management"]
)


@router.post(
    "/",
    response_model=StreetLightManagementResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Créer un street_light_management"
)
async def create(
    data: StreetLightManagementCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Créer un nouveau street_light_management
    
    - **data**: Données du street_light_management à créer
    """
    return await create_street_light_management(data, db)


@router.get(
    "/{item_id}",
    response_model=StreetLightManagementResponse,
    summary="Récupérer un street_light_management par ID"
)
async def get_by_id(
    item_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Récupérer un street_light_management spécifique par son ID
    
    - **item_id**: ID du street_light_management
    """
    return await get_street_light_management_by_id(item_id, db)


@router.get(
    "/",
    response_model=List[StreetLightManagementResponse],
    summary="Lister tous les street_light_management"
)
async def get_all(
    skip: int = Query(0, ge=0, description="Nombre d'éléments à sauter"),
    limit: int = Query(20, ge=1, le=100, description="Nombre d'éléments à retourner"),
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Récupérer la liste de tous les street_light_management
    
    - **skip**: Pagination - nombre d'éléments à sauter
    - **limit**: Pagination - nombre maximum d'éléments à retourner
    """
    return await get_all_street_light_management(db, skip, limit)


@router.put(
    "/{item_id}",
    response_model=StreetLightManagementResponse,
    summary="Mettre à jour un street_light_management"
)
async def update(
    item_id: UUID,
    data: StreetLightManagementUpdate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Mettre à jour un street_light_management existant
    
    - **item_id**: ID du street_light_management
    - **data**: Données à mettre à jour
    """
    return await update_street_light_management(item_id, data, db)


@router.delete(
    "/{item_id}",
    status_code=status.HTTP_200_OK,
    summary="Supprimer un street_light_management"
)
async def delete(
    item_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Supprimer un street_light_management
    
    - **item_id**: ID du street_light_management à supprimer
    """
    return await delete_street_light_management(item_id, db)
