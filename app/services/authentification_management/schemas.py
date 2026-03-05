"""
Schémas Pydantic pour le service Authentification Managment
"""

from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field
from fastapi import status

class LoginRequest(BaseModel):
    access_login: str
    password: str

class UserCreateRequest(BaseModel):
    access_login : str
    password : str
    email : str
    name: str = "Inonnu"

class TokenResponse(BaseModel):
    status_code : Optional[int] = status.HTTP_200_OK
    message : Optional[str] = None
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    user_id: str | None = None
    
