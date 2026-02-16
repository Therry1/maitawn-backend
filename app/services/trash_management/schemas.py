"""
Schémas Pydantic pour le service Trash Management
"""

from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field

from app.services.trash_management.constants import TrashManagementStatus, TrashManagementType


class TrashManagementBase(BaseModel):
    """Schéma de base pour trash_management"""
    name: str = Field(..., min_length=1, max_length=255, description="Nom du trash_management")
    description: Optional[str] = Field(None, max_length=1000, description="Description")
    status: TrashManagementStatus = Field(default=TrashManagementStatus.ACTIVE, description="Statut")
    type: TrashManagementType = Field(..., description="Type de trash_management")


class TrashManagementCreate(TrashManagementBase):
    """Schéma pour la création d'un trash_management"""
    # Ajoutez ici les champs spécifiques à la création
    pass


class TrashManagementUpdate(BaseModel):
    """Schéma pour la mise à jour d'un trash_management"""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    status: Optional[TrashManagementStatus] = None
    type: Optional[TrashManagementType] = None


class TrashManagementResponse(TrashManagementBase):
    """Schéma de réponse pour un trash_management"""
    id: UUID = Field(..., description="ID unique")
    created_at: datetime = Field(..., description="Date de création")
    updated_at: Optional[datetime] = Field(None, description="Date de dernière modification")
    
    class Config:
        from_attributes = True


class TrashManagementList(BaseModel):
    """Schéma pour une liste paginée de trash_management"""
    items: list[TrashManagementResponse]
    total: int
    skip: int
    limit: int
