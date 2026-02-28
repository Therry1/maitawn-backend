from fastapi import HTTPException, status



class PushNotificationClass():
    
    async def sendNotification ():
        try:
            
            
            return "ok"
        except Exception as exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail= f"error push Notification: Exception: {str(exception)}"
            )