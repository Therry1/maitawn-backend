import os
from uuid import uuid4, UUID
from fastapi import UploadFile, HTTPException
import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),
    api_key=os.environ.get("CLOUDINARY_API_KEY"),
    api_secret=os.environ.get("CLOUDINARY_API_SECRET")
)

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".pdf"}

async def save_uploaded_file(file: UploadFile, institution_id: UUID):
    _, extension = os.path.splitext(file.filename)
    extension = extension.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Extension non autorisée")

    content = await file.read()
    
    result = cloudinary.uploader.upload(
        content,
        folder=f"uploads/{institution_id}",
        public_id=str(uuid4()),
        resource_type="auto"
    )

    file_url = result["secure_url"]
    new_filename = result["public_id"].split("/")[-1]

    return new_filename, file_url
