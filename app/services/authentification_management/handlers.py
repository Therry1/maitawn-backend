"""
Handlers pour le service Authentification Managment

Contient la logique métier du service
"""

import asyncio
from datetime import datetime
import hashlib
from uuid import uuid4
from fastapi import HTTPException, status
from app.services.authentification_management.dependencies import create_access_token, create_refresh_token, verify_token
from app.services.authentification_management.schemas import LoginRequest, TokenResponse, UserCreateRequest

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(plain: str, hashed: str) -> bool:
    return hash_password(plain) == hashed

async def register (db , first_account_data:UserCreateRequest):
    try:
        # 3. Créer le compte
        new_account = {
            "access_login": first_account_data.access_login,
            "password": hash_password(first_account_data.password),
            "name": first_account_data.name,
            "email": first_account_data.email,
            "created_at": datetime.utcnow().isoformat()
        }
        
        account_id = str(uuid4())
        doc_ref = db.collection("users").document(account_id)

        await asyncio.to_thread(
            lambda: doc_ref.set(new_account)
        )

        # 4. Retourner les tokens comme pour le login
        access_token = create_access_token(doc_ref.id)
        refresh_token = create_refresh_token(doc_ref.id)
        
        return TokenResponse(
            message = "compte créé avec succès",
            access_token=access_token,
            refresh_token=refresh_token
        )
    except Exception as exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"UnAutorize {str(exception)}"
        )

async def login(db, payload: LoginRequest) -> TokenResponse:
    # Chercher l'utilisateur dans Firestore
    users_ref = db.collection("users")

    query = await asyncio.to_thread(
        lambda: users_ref.where("access_login", "==", payload.access_login)
        .limit(1)
        .get()
    )

    if not query:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="UnAuthorize"
        )

    user = query[0].to_dict()
    user_id = query[0].id

    if not verify_password(payload.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="login d'accès ou mot de passe incorrect"
        )

    access_token = create_access_token(user_id)
    refresh_token = create_refresh_token(user_id)

    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token
    )

async def refresh_token(db, token: str) -> TokenResponse:
    user_id = verify_token(token, token_type="refresh")

    # Vérifier que l'utilisateur existe toujours
    user_doc = await asyncio.to_thread(
        lambda: db.collection("institution_account_users").document(user_id).get()
    )
    if not user_doc.exists:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")

    return TokenResponse(
        access_token=create_access_token(user_id),
        refresh_token=create_refresh_token(user_id)
    )