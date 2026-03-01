"""
Schémas Pydantic pour le service Institution Management
"""

from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from google.cloud.firestore_v1 import GeoPoint

from app.services.institution_management.constants import InstitutionManagementStatus, InstitutionManagementType

class RegionResponse(BaseModel):
    id: UUID
    name: str
    created_at: Optional[datetime] = None


class DepartmentResponse(BaseModel):
    id: UUID
    name: str
    region_id: UUID
    created_at: Optional[datetime] = None


class ArrondissementResponse(BaseModel):
    id: UUID
    name: str
    department_id: Optional[UUID] = None
    created_at: Optional[datetime] = None
    
class InstitutionCategoryBase(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    label: str
    code: str
    type: int
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None

class InstitutionCategoryResponse(BaseModel):
    id: UUID
    label: str
    code: str
    type: int
    created_at: datetime
    updated_at: Optional[datetime] = None

class LocationModel(BaseModel):
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)

    def to_geopoint(self) -> GeoPoint:
        return GeoPoint(self.latitude, self.longitude)
    
class InstitutionBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255, description="Nom du institution_management")
    description: Optional[str] = Field(None, max_length=1000, description="Description")
    status: InstitutionManagementStatus = Field(default=InstitutionManagementStatus.ACTIVE, description="Statut")
    #type: InstitutionManagementType = Field(..., description="Type de institution_management")


class InstitutionCreate(InstitutionBase):
    id: UUID = Field(default_factory=uuid4)
    region_id : UUID
    department_id : UUID
    arrondissement_id : UUID
    category_id: UUID
    location: LocationModel
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    
class InstitutionAccountRequest(BaseModel):
    access_login : str
    password : str
    email : str
    autor_name: str = "Inonnu"
    institution_id: UUID
    

class InstitutionUpdate(BaseModel):
    """Schéma pour la mise à jour d'un institution_management"""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    status: Optional[InstitutionManagementStatus] = None
    type: Optional[InstitutionManagementType] = None


class InstitutionResponse(InstitutionBase):
    """Schéma de réponse pour un institution_management"""
    id: UUID = Field(..., description="ID unique")
    created_at: datetime = Field(..., description="Date de création")
    updated_at: Optional[datetime] = Field(None, description="Date de dernière modification")
    
    class Config:
        from_attributes = True


class InstitutionList(BaseModel):
    """Schéma pour une liste paginée de institution_management"""
    items: list[InstitutionResponse]
    total: int
    skip: int
    limit: int
