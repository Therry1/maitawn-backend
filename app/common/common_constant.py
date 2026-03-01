from enum import IntEnum

class DeviceType(int, IntEnum):
    """Device platform types for OneSignal"""
    IOS = 0
    ANDROID = 1
    AMAZON = 2
    WINDOWS_PHONE = 3

class NotificationType(int, IntEnum):
    """Notification subscription status"""
    SUBSCRIBED = 1
    UNSUBSCRIBED = -2
    NO_PERMISSION = 0

GET_METHOD = "GET"
POST_METHOD = "POST"
PUT_METHOD = "PUT"
DELETE_METHOD = "DELETE"
