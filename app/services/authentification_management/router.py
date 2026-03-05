"""
Routes pour le service Authentification Managment
"""

from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession


from fastapi import APIRouter, Depends
from app.services.authentification_management.schemas import LoginRequest, TokenResponse, UserCreateRequest
from app.services.authentification_management.handlers import login, refresh_token, register
from app.services.authentification_management.dependencies import get_current_user
from firebase import get_firebase_db
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["Auth"])

class RefreshRequest(BaseModel):
    refresh_token: str

@router.post("/register", response_model=TokenResponse)
async def register_route(payload: UserCreateRequest):
    db = get_firebase_db()
    return await register(db, payload)

@router.post("/login", response_model=TokenResponse)
async def login_route(payload: LoginRequest):
    db = get_firebase_db()
    return await login(db, payload)

@router.post("/refresh", response_model=TokenResponse)
async def refresh_route(payload: RefreshRequest):
    db = get_firebase_db()
    return await refresh_token(db, payload.refresh_token)

@router.get("/me")
async def me(user_id: str = Depends(get_current_user)):
    return {"user_id": user_id}