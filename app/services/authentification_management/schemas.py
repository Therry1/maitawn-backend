"""
Schémas Pydantic pour le service Authentification Managment
"""

from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field

class LoginRequest(BaseModel):
    access_login: str
    password: str

class TokenResponse(BaseModel):
    message : Optional[str] = None
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    user_id: str | None = None
    
