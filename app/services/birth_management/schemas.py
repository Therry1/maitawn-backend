"""
Schémas Pydantic pour le service Birth Management
"""

from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field

from app.services.birth_management.constants import BirthManagementStatus, BirthManagementType


class BirthManagementBase(BaseModel):
    """Schéma de base pour birth_management"""
    name: str = Field(..., min_length=1, max_length=255, description="Nom du birth_management")
    description: Optional[str] = Field(None, max_length=1000, description="Description")
    status: BirthManagementStatus = Field(default=BirthManagementStatus.ACTIVE, description="Statut")
    type: BirthManagementType = Field(..., description="Type de birth_management")


class BirthManagementCreate(BirthManagementBase):
    """Schéma pour la création d'un birth_management"""
    # Ajoutez ici les champs spécifiques à la création
    pass


class BirthManagementUpdate(BaseModel):
    """Schéma pour la mise à jour d'un birth_management"""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    status: Optional[BirthManagementStatus] = None
    type: Optional[BirthManagementType] = None


class BirthManagementResponse(BirthManagementBase):
    """Schéma de réponse pour un birth_management"""
    id: UUID = Field(..., description="ID unique")
    created_at: datetime = Field(..., description="Date de création")
    updated_at: Optional[datetime] = Field(None, description="Date de dernière modification")
    
    class Config:
        from_attributes = True


class BirthManagementList(BaseModel):
    """Schéma pour une liste paginée de birth_management"""
    items: list[BirthManagementResponse]
    total: int
    skip: int
    limit: int
