from fastapi_mail import MessageSchema, MessageType
from app.config.email import fast_mail

async def send_email(
    recipients: list[str],
    subject: str,
    body: str,
):
    message = MessageSchema(
        subject=subject,
        recipients=recipients,
        body=body,
        subtype=MessageType.html  # ou MessageType.plain pour du texte simple
    )

    await fast_mail.send_message(message)