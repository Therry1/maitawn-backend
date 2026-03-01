"""
Routes pour le service Institution Management
"""
from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, status, Query

from app.services.institution_management.schemas import (
    ArrondissementResponse,
    DepartmentResponse,
    InstitutionAccountRequest,
    InstitutionCategoryResponse,
    InstitutionCreate,
    InstitutionResponse,
    InstitutionUpdate,
    RegionResponse
)
from app.services.institution_management.handlers import (
    create_institution_categories,
    create_institution_management,
    get_institution_by_id,
    init_locations,
    list_arrondissements,
    list_departments,
    list_institution_categories,
    list_institutions,
    list_regions
)
from firebase import get_firebase_db
db = get_firebase_db()

router = APIRouter(
    prefix="/institution_management",
    tags=["Institution Management"]
)

@router.get("/region")
async def regions():
    return {"regions": ["test1", "test2"]}

@router.post("/init-locations")
async def init_locations_path():
    return await init_locations(db)

@router.get("/regions", response_model=list[RegionResponse])
async def get_regions_path():
    return await list_regions(db)


@router.get("/departments", response_model=list[DepartmentResponse])
async def get_departments_path():
    return await list_departments(db)

@router.get("/arrondissements", response_model=list[ArrondissementResponse])
async def get_arrondissements_path():
    return await list_arrondissements(db)


@router.post(
    "/institution-category",
    status_code=status.HTTP_201_CREATED,
    summary="Créer un institution_management"
)
async def create():
    """
    Créer une nouvelle categorie d'institution
    """
    return await create_institution_categories(db)

@router.get(
    "/institution-category",
    response_model=List[InstitutionCategoryResponse],
    status_code=status.HTTP_200_OK
)
async def get_institution_categories():
    return await list_institution_categories(db)

@router.post(
    "/institution",
    #response_model  =InstitutionResponse,
    status_code     =status.HTTP_201_CREATED,
    summary         ="Créer une institution"
)
async def create(
    institution_data: InstitutionCreate,
    first_account_data : InstitutionAccountRequest
):
    """
    Créer une nouveau nouvelle institution
    """
    return await create_institution_management(institution_data,first_account_data, db)

@router.get(
    "/institutions",
    response_model=List[InstitutionResponse],
    status_code=status.HTTP_200_OK,
    summary="Lister toutes les institutions"
)
async def get_all_institutions():
    return await list_institutions(db)


@router.get(
    '/institutions/{institution_id}',
    status_code= status.HTTP_200_OK,
    summary= "route permmetant de rechercher une institution"
)
async def get_institution_by_id_path(institution_id: UUID):
    return await get_institution_by_id(db , institution_id)