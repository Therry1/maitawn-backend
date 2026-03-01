import os
from uuid import uuid4, UUID
from fastapi import UploadFile, HTTPException
import firebase_admin
from firebase_admin import storage

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".pdf"}

async def save_uploaded_file(file: UploadFile, institution_id: UUID):
    # 1. Vérifier extension
    filename = file.filename
    _, extension = os.path.splitext(filename)
    extension = extension.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Extension non autorisée")

    # 2. Renommer le fichier
    new_filename = f"{uuid4()}{extension}"

    # 3. Chemin dans Firebase Storage
    destination = f"uploads/{institution_id}/{new_filename}"

    # 4. Upload vers Firebase Storage
    bucket = storage.bucket()
    blob = bucket.blob(destination)

    content = await file.read()
    blob.upload_from_string(content, content_type=file.content_type)

    # 5. Rendre le fichier public et récupérer l'URL
    blob.make_public()
    file_url = blob.public_url

    return new_filename, file_url