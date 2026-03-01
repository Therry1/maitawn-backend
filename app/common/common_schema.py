from typing import Dict, Optional

from pydantic import BaseModel

from app.common.common_constant import DeviceType, NotificationType


class NotificationRequestSchema(BaseModel):
    content: str

class OneSignalUser(BaseModel):
    """OneSignal User/Device Model"""
    
    app_id: str 
    device_type: DeviceType
    
    identifier: Optional[str] = None
    language: Optional[str] = None
    timezone: Optional[int]  = None
    game_version: Optional[str]  = None
    device_model: Optional[str]  = None
    device_os: Optional[str] = None
    ad_id: Optional[str]  = None
    sdk: Optional[str]  = None
    session_count: Optional[int] = None
    tags: Optional[Dict[str, str]] = None
    external_user_id: Optional[str]  = None
    notification_types: Optional[NotificationType] = None
