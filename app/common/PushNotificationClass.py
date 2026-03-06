from fastapi import HTTPException, status
import os

import httpx

from app.common.common_constant import POST_METHOD
from app.common.common_schema import OneSignalUser
from app.services.email_service import send_email
ONESIGNAL_APP_ID= os.environ.get('ONESIGNAL_APP_ID')
ONESIGNAL_REST_KEY= os.environ.get('ONESIGNAL_REST_KEY')
ONESIGNAL_BASE_URL = os.environ.get('ONESIGNAL_BASE_URL')


class PushNotificationClass():
    
    async def add_player(user_data : OneSignalUser):
        try:
            # construction de l'entete de la requete
            headers = {
                'Content-Type' : 'application/json',
                'Authorization': 'Basic '+str(ONESIGNAL_APP_ID)
            }
            
            params = {}
            
            # construction de l'url de la requete
            base_url = ONESIGNAL_BASE_URL.rstrip('/')
            add_player_path = '/v1/players'
            final_url = base_url + add_player_path
            
            # methode de la requete
            
            async with httpx.AsyncClient() as client:
                response = await client.request(
                    method=POST_METHOD.upper(),
                    url=final_url,
                    headers=headers,
                    json=user_data.model_dump(),
                    params=params,
                    data=user_data.model_dump(),
                )

                if response.status_code >= 400:
                    raise HTTPException(
                        status_code=response.status_code,
                        detail=response.json()
                    )

                return response.json()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail= f"error adding player for push Notification. http request doesn't execute"
            )
        except Exception as exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail= f"error adding player for push Notification: Exception: {str(exception)}"
            )
            
    async def sendNotification ():
        try:
            header = {
                'Content-Type' : 'application/json',
                'Authorization': 'Basic '+str(ONESIGNAL_APP_ID)
            }
            
            return "ok"
        except Exception as exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail= f"error push Notification: Exception: {str(exception)}"
            )
            

async def send_notification(recipient_email: str ,  description:str = "Nouvelle alerte Aucune description mentionné" , lieu: str="Auncun lieu signalé"):
    try:
        await send_email(
            recipients=[recipient_email , "therrynganga5@gmail.com"],
            subject="Vous avez recu une nouvelle alerte",
            body="<h1>Desciption: </h1><p>"+description+" à "+ lieu +"</p>"
        )
        print("message:Email envoyé avec succès")
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )