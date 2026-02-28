"""
Schémas Pydantic pour le service Post Alert Management
"""

from datetime import datetime
from typing import Annotated, List, Optional
from uuid import UUID
from fastapi import File, Form, UploadFile
from pydantic import BaseModel, ConfigDict, Field
from google.cloud.firestore_v1 import GeoPoint

from app.services.post_alert_management.constants import ValidationState


class LocationModel(BaseModel):
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)

    def to_geopoint(self) -> GeoPoint:
        return GeoPoint(self.latitude, self.longitude)


class PostAlertBase(BaseModel):
    post_category_id: UUID
    latitude: float 
    longitude: float 
    
    model_config = ConfigDict(extra="ignore")
    
    #attachment: UploadFile

    # @classmethod
    # def as_form(
    #     cls,
    #     post_category_id: Annotated[UUID, Form()],
    #     latitude: Annotated[float, Form()],
    #     longitude: Annotated[float, Form()],
    #     attachment: Annotated[UploadFile, File()],
    # ):
    #     location = LocationModel(
    #         latitude=latitude,
    #         longitude=longitude
    #     )

    #     return cls(
    #         post_category_id=post_category_id,
    #         location=location,
    #         attachment=attachment
    #     )

class PostAlertForm:
    def __init__(
        self,
        post_category_id: Annotated[UUID, Form(...)],
        latitude: Annotated[float, Form(...)],
        longitude: Annotated[float, Form(...)],
        attachment: Annotated[UploadFile, File(...)]
    ):
        self.post_category_id = post_category_id
        self.latitude = latitude
        self.longitude = longitude
        self.attachment = attachment

    def to_schema(self) -> PostAlertBase:
        return PostAlertBase(
            post_category_id=self.post_category_id,
            location=LocationModel(
                latitude=self.latitude,
                longitude=self.longitude
            )
        )
        
class PostAlertSchemaStore(BaseModel):
    post_category_id: str
    institution_ids : List[str]
    location: LocationModel
    file_name: str
    file_url : str
    created_at: datetime
    state : ValidationState

class PostAlertResponse(BaseModel):
    post_category_id: str
    institution_id : List[str]
    latitude: float 
    longitude: float
    file_name: Optional[str] = None
    file_url : Optional[str] = None
    created_at: Optional[datetime] = None
    state : ValidationState
    