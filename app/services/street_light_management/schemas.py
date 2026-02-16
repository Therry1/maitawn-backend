"""
Schémas Pydantic pour le service Street Light Management
"""

from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field

from app.services.street_light_management.constants import StreetLightManagementStatus, StreetLightManagementType


class StreetLightManagementBase(BaseModel):
    """Schéma de base pour street_light_management"""
    name: str = Field(..., min_length=1, max_length=255, description="Nom du street_light_management")
    description: Optional[str] = Field(None, max_length=1000, description="Description")
    status: StreetLightManagementStatus = Field(default=StreetLightManagementStatus.ACTIVE, description="Statut")
    type: StreetLightManagementType = Field(..., description="Type de street_light_management")


class StreetLightManagementCreate(StreetLightManagementBase):
    """Schéma pour la création d'un street_light_management"""
    # Ajoutez ici les champs spécifiques à la création
    pass


class StreetLightManagementUpdate(BaseModel):
    """Schéma pour la mise à jour d'un street_light_management"""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    status: Optional[StreetLightManagementStatus] = None
    type: Optional[StreetLightManagementType] = None


class StreetLightManagementResponse(StreetLightManagementBase):
    """Schéma de réponse pour un street_light_management"""
    id: UUID = Field(..., description="ID unique")
    created_at: datetime = Field(..., description="Date de création")
    updated_at: Optional[datetime] = Field(None, description="Date de dernière modification")
    
    class Config:
        from_attributes = True


class StreetLightManagementList(BaseModel):
    """Schéma pour une liste paginée de street_light_management"""
    items: list[StreetLightManagementResponse]
    total: int
    skip: int
    limit: int
