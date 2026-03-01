import os
import shutil
from uuid import uuid4, UUID
from fastapi import UploadFile, HTTPException , status

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".pdf"}

BASE_UPLOAD_DIR = "uploads"  # dossier racine


async def save_uploaded_file(file: UploadFile, institution_id: UUID):

    # try:
        # 1️⃣ Vérifier extension
    filename = file.filename
    _, extension = os.path.splitext(filename)

    extension = extension.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Extension non autorisée"
        )

    # 2️⃣ Renommer le fichier
    new_filename = f"{uuid4()}{extension}"

    # 3️⃣ Construire chemin institution
    institution_folder = os.path.join(
        BASE_UPLOAD_DIR,
        str(institution_id)
    )

    # 4️⃣ Créer dossier si inexistant
    os.makedirs(institution_folder, exist_ok=True)

    # 5️⃣ Chemin final du fichier
    file_path = os.path.join(institution_folder, new_filename)

    # 6️⃣ Sauvegarde physique
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return new_filename , file_path
    # except Exception as exception:
    #     raise HTTPException(
    #         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #         detail= f"une erreur s'est produite lors de l'upload du fichier. {str(exception)}"
    #     )