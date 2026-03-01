"""
Routes pour le repertoire common
"""
from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, status, Query

from app.common.PushNotificationClass import PushNotificationClass
from app.common.common_constant import DeviceType
from app.common.common_schema import OneSignalUser
from firebase import get_firebase_db
db = get_firebase_db()

router = APIRouter(
    prefix="/common",
    tags=["Common roads"]
)

@router.post(
    '/testNotif'
)
async def test_notification_class():
    test = OneSignalUser(app_id="azazazezezezez" , device_type= DeviceType.ANDROID)
    return await PushNotificationClass.add_player(test)
