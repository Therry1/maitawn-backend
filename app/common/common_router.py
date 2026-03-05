"""
Routes pour le repertoire common
"""
from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status, Query

from app.common.PushNotificationClass import PushNotificationClass
from app.common.common_constant import DeviceType
from app.common.common_schema import OneSignalUser
from app.services.email_service import send_email
from firebase import get_firebase_db
db = get_firebase_db()

router = APIRouter(
    prefix="/common",
    tags=["Common roads"]
)

@router.get(
    "/send-email",
    status_code=status.HTTP_200_OK
)
async def send_notification(recipient_email: str):
    try:
        await send_email(
            recipients=[recipient_email],
            subject="Nouvelle alerte",
            body="<h1>Bonjour</h1><p>Vous avez une nouvelle notification.</p>"
        )
        return {"message": "Email envoyé avec succès"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )