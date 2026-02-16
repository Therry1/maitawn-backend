"""
Routes pour le service Trash Management
"""

from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database import get_db
from app.common.auth import get_current_user
from app.services.trash_management.schemas import (
    TrashManagementCreate,
    TrashManagementUpdate,
    TrashManagementResponse
)
from app.services.trash_management.handlers import (
    create_trash_management,
    get_trash_management_by_id,
    get_all_trash_management,
    update_trash_management,
    delete_trash_management
)

router = APIRouter(
    prefix="/trash_management",
    tags=["Trash Management"]
)


@router.post(
    "/",
    response_model=TrashManagementResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Créer un trash_management"
)
async def create(
    data: TrashManagementCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Créer un nouveau trash_management
    
    - **data**: Données du trash_management à créer
    """
    return await create_trash_management(data, db)


@router.get(
    "/{item_id}",
    response_model=TrashManagementResponse,
    summary="Récupérer un trash_management par ID"
)
async def get_by_id(
    item_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Récupérer un trash_management spécifique par son ID
    
    - **item_id**: ID du trash_management
    """
    return await get_trash_management_by_id(item_id, db)


@router.get(
    "/",
    response_model=List[TrashManagementResponse],
    summary="Lister tous les trash_management"
)
async def get_all(
    skip: int = Query(0, ge=0, description="Nombre d'éléments à sauter"),
    limit: int = Query(20, ge=1, le=100, description="Nombre d'éléments à retourner"),
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Récupérer la liste de tous les trash_management
    
    - **skip**: Pagination - nombre d'éléments à sauter
    - **limit**: Pagination - nombre maximum d'éléments à retourner
    """
    return await get_all_trash_management(db, skip, limit)


@router.put(
    "/{item_id}",
    response_model=TrashManagementResponse,
    summary="Mettre à jour un trash_management"
)
async def update(
    item_id: UUID,
    data: TrashManagementUpdate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Mettre à jour un trash_management existant
    
    - **item_id**: ID du trash_management
    - **data**: Données à mettre à jour
    """
    return await update_trash_management(item_id, data, db)


@router.delete(
    "/{item_id}",
    status_code=status.HTTP_200_OK,
    summary="Supprimer un trash_management"
)
async def delete(
    item_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Supprimer un trash_management
    
    - **item_id**: ID du trash_management à supprimer
    """
    return await delete_trash_management(item_id, db)
