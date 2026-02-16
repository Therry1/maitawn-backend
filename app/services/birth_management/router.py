"""
Routes pour le service Birth Management
"""

from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database import get_db
from app.common.auth import get_current_user
from app.services.birth_management.schemas import (
    BirthManagementCreate,
    BirthManagementUpdate,
    BirthManagementResponse
)
from app.services.birth_management.handlers import (
    create_birth_management,
    get_birth_management_by_id,
    get_all_birth_management,
    update_birth_management,
    delete_birth_management
)

router = APIRouter(
    prefix="/birth_management",
    tags=["Birth Management"]
)


@router.post(
    "/",
    response_model=BirthManagementResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Créer un birth_management"
)
async def create(
    data: BirthManagementCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Créer un nouveau birth_management
    
    - **data**: Données du birth_management à créer
    """
    return await create_birth_management(data, db)


@router.get(
    "/{item_id}",
    response_model=BirthManagementResponse,
    summary="Récupérer un birth_management par ID"
)
async def get_by_id(
    item_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Récupérer un birth_management spécifique par son ID
    
    - **item_id**: ID du birth_management
    """
    return await get_birth_management_by_id(item_id, db)


@router.get(
    "/",
    response_model=List[BirthManagementResponse],
    summary="Lister tous les birth_management"
)
async def get_all(
    skip: int = Query(0, ge=0, description="Nombre d'éléments à sauter"),
    limit: int = Query(20, ge=1, le=100, description="Nombre d'éléments à retourner"),
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Récupérer la liste de tous les birth_management
    
    - **skip**: Pagination - nombre d'éléments à sauter
    - **limit**: Pagination - nombre maximum d'éléments à retourner
    """
    return await get_all_birth_management(db, skip, limit)


@router.put(
    "/{item_id}",
    response_model=BirthManagementResponse,
    summary="Mettre à jour un birth_management"
)
async def update(
    item_id: UUID,
    data: BirthManagementUpdate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Mettre à jour un birth_management existant
    
    - **item_id**: ID du birth_management
    - **data**: Données à mettre à jour
    """
    return await update_birth_management(item_id, data, db)


@router.delete(
    "/{item_id}",
    status_code=status.HTTP_200_OK,
    summary="Supprimer un birth_management"
)
async def delete(
    item_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Supprimer un birth_management
    
    - **item_id**: ID du birth_management à supprimer
    """
    return await delete_birth_management(item_id, db)
