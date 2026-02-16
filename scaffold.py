#!/usr/bin/env python3
"""
Script de génération automatique de services FastAPI
Usage: python scaffold.py <nom_du_service>
Exemple: python scaffold.py users
"""

import os
import sys
from pathlib import Path
from datetime import datetime


def to_snake_case(name: str) -> str:
    """Convertir en snake_case"""
    return name.lower().replace("-", "_").replace(" ", "_")


def to_pascal_case(name: str) -> str:
    """Convertir en PascalCase"""
    return "".join(word.capitalize() for word in name.replace("-", "_").replace(" ", "_").split("_"))


def to_title(name: str) -> str:
    """Convertir en Title Case"""
    return " ".join(word.capitalize() for word in name.replace("-", " ").replace("_", " ").split())


def create_handlers_file(service_path: Path, service_name: str):
    """Créer le fichier handlers.py"""
    pascal_name = to_pascal_case(service_name)
    
    content = f'''"""
Handlers pour le service {to_title(service_name)}
Contient la logique métier du service
"""

from typing import List, Optional
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status

from app.services.{service_name}.schemas import (
    {pascal_name}Create,
    {pascal_name}Update,
    {pascal_name}Response
)
# from app.common.models.{pascal_name} import {pascal_name}


async def create_{service_name}(
    data: {pascal_name}Create,
    db: AsyncSession
) -> {pascal_name}Response:
    """
    Créer un nouveau {service_name}
    
    Args:
        data: Données de création
        db: Session de base de données
    
    Returns:
        {pascal_name}Response: L'objet créé
    
    Raises:
        HTTPException: Si une erreur survient
    """
    # TODO: Implémenter la logique de création
    # new_item = {pascal_name}(**data.model_dump())
    # db.add(new_item)
    # await db.commit()
    # await db.refresh(new_item)
    # return new_item
    
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Cette fonctionnalité n'est pas encore implémentée"
    )


async def get_{service_name}_by_id(
    item_id: UUID,
    db: AsyncSession
) -> {pascal_name}Response:
    """
    Récupérer un {service_name} par son ID
    
    Args:
        item_id: ID de l'objet
        db: Session de base de données
    
    Returns:
        {pascal_name}Response: L'objet trouvé
    
    Raises:
        HTTPException: Si l'objet n'existe pas
    """
    # TODO: Implémenter la logique de récupération
    # item = await db.get({pascal_name}, item_id)
    # if not item:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f"{pascal_name} not found"
    #     )
    # return item
    
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Cette fonctionnalité n'est pas encore implémentée"
    )


async def get_all_{service_name}(
    db: AsyncSession,
    skip: int = 0,
    limit: int = 100
) -> List[{pascal_name}Response]:
    """
    Récupérer tous les {service_name}
    
    Args:
        db: Session de base de données
        skip: Nombre d'éléments à sauter
        limit: Nombre maximum d'éléments à retourner
    
    Returns:
        List[{pascal_name}Response]: Liste des objets
    """
    # TODO: Implémenter la logique de récupération
    # stmt = select({pascal_name}).offset(skip).limit(limit)
    # result = await db.execute(stmt)
    # items = result.scalars().all()
    # return items
    
    return []


async def update_{service_name}(
    item_id: UUID,
    data: {pascal_name}Update,
    db: AsyncSession
) -> {pascal_name}Response:
    """
    Mettre à jour un {service_name}
    
    Args:
        item_id: ID de l'objet
        data: Données de mise à jour
        db: Session de base de données
    
    Returns:
        {pascal_name}Response: L'objet mis à jour
    
    Raises:
        HTTPException: Si l'objet n'existe pas
    """
    # TODO: Implémenter la logique de mise à jour
    # item = await db.get({pascal_name}, item_id)
    # if not item:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f"{pascal_name} not found"
    #     )
    # 
    # for key, value in data.model_dump(exclude_unset=True).items():
    #     setattr(item, key, value)
    # 
    # await db.commit()
    # await db.refresh(item)
    # return item
    
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Cette fonctionnalité n'est pas encore implémentée"
    )


async def delete_{service_name}(
    item_id: UUID,
    db: AsyncSession
) -> dict:
    """
    Supprimer un {service_name}
    
    Args:
        item_id: ID de l'objet
        db: Session de base de données
    
    Returns:
        dict: Message de confirmation
    
    Raises:
        HTTPException: Si l'objet n'existe pas
    """
    # TODO: Implémenter la logique de suppression
    # item = await db.get({pascal_name}, item_id)
    # if not item:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f"{pascal_name} not found"
    #     )
    # 
    # await db.delete(item)
    # await db.commit()
    # return {{"message": f"{pascal_name} deleted successfully"}}
    
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Cette fonctionnalité n'est pas encore implémentée"
    )
'''
    
    with open(service_path / "handlers.py", "w", encoding="utf-8") as f:
        f.write(content)


def create_constants_file(service_path: Path, service_name: str):
    """Créer le fichier constants.py"""
    pascal_name = to_pascal_case(service_name)
    
    content = f'''"""
Constantes pour le service {to_title(service_name)}
"""

from enum import Enum


class {pascal_name}Status(str, Enum):
    """Statuts possibles pour {service_name}"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
    ARCHIVED = "archived"


class {pascal_name}Type(str, Enum):
    """Types possibles pour {service_name}"""
    TYPE_A = "type_a"
    TYPE_B = "type_b"
    TYPE_C = "type_c"


# Constantes de configuration
MAX_{service_name.upper()}_PER_PAGE = 100
DEFAULT_{service_name.upper()}_LIMIT = 20

# Messages d'erreur
ERROR_NOT_FOUND = "{pascal_name} not found"
ERROR_ALREADY_EXISTS = "{pascal_name} already exists"
ERROR_INVALID_STATUS = "Invalid {service_name} status"
ERROR_UNAUTHORIZED = "Unauthorized to access this {service_name}"

# Messages de succès
SUCCESS_CREATED = "{pascal_name} created successfully"
SUCCESS_UPDATED = "{pascal_name} updated successfully"
SUCCESS_DELETED = "{pascal_name} deleted successfully"
'''
    
    with open(service_path / "constants.py", "w", encoding="utf-8") as f:
        f.write(content)


def create_router_file(service_path: Path, service_name: str):
    """Créer le fichier router.py"""
    pascal_name = to_pascal_case(service_name)
    
    content = f'''"""
Routes pour le service {to_title(service_name)}
"""

from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database import get_db
from app.common.auth import get_current_user
from app.services.{service_name}.schemas import (
    {pascal_name}Create,
    {pascal_name}Update,
    {pascal_name}Response
)
from app.services.{service_name}.handlers import (
    create_{service_name},
    get_{service_name}_by_id,
    get_all_{service_name},
    update_{service_name},
    delete_{service_name}
)

router = APIRouter(
    prefix="/{service_name}",
    tags=["{to_title(service_name)}"]
)


@router.post(
    "/",
    response_model={pascal_name}Response,
    status_code=status.HTTP_201_CREATED,
    summary="Créer un {service_name}"
)
async def create(
    data: {pascal_name}Create,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Créer un nouveau {service_name}
    
    - **data**: Données du {service_name} à créer
    """
    return await create_{service_name}(data, db)


@router.get(
    "/{{item_id}}",
    response_model={pascal_name}Response,
    summary="Récupérer un {service_name} par ID"
)
async def get_by_id(
    item_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Récupérer un {service_name} spécifique par son ID
    
    - **item_id**: ID du {service_name}
    """
    return await get_{service_name}_by_id(item_id, db)


@router.get(
    "/",
    response_model=List[{pascal_name}Response],
    summary="Lister tous les {service_name}"
)
async def get_all(
    skip: int = Query(0, ge=0, description="Nombre d'éléments à sauter"),
    limit: int = Query(20, ge=1, le=100, description="Nombre d'éléments à retourner"),
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Récupérer la liste de tous les {service_name}
    
    - **skip**: Pagination - nombre d'éléments à sauter
    - **limit**: Pagination - nombre maximum d'éléments à retourner
    """
    return await get_all_{service_name}(db, skip, limit)


@router.put(
    "/{{item_id}}",
    response_model={pascal_name}Response,
    summary="Mettre à jour un {service_name}"
)
async def update(
    item_id: UUID,
    data: {pascal_name}Update,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Mettre à jour un {service_name} existant
    
    - **item_id**: ID du {service_name}
    - **data**: Données à mettre à jour
    """
    return await update_{service_name}(item_id, data, db)


@router.delete(
    "/{{item_id}}",
    status_code=status.HTTP_200_OK,
    summary="Supprimer un {service_name}"
)
async def delete(
    item_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Supprimer un {service_name}
    
    - **item_id**: ID du {service_name} à supprimer
    """
    return await delete_{service_name}(item_id, db)
'''
    
    with open(service_path / "router.py", "w", encoding="utf-8") as f:
        f.write(content)


def create_schemas_file(service_path: Path, service_name: str):
    """Créer le fichier schemas.py"""
    pascal_name = to_pascal_case(service_name)
    
    content = f'''"""
Schémas Pydantic pour le service {to_title(service_name)}
"""

from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field

from app.services.{service_name}.constants import {pascal_name}Status, {pascal_name}Type


class {pascal_name}Base(BaseModel):
    """Schéma de base pour {service_name}"""
    name: str = Field(..., min_length=1, max_length=255, description="Nom du {service_name}")
    description: Optional[str] = Field(None, max_length=1000, description="Description")
    status: {pascal_name}Status = Field(default={pascal_name}Status.ACTIVE, description="Statut")
    type: {pascal_name}Type = Field(..., description="Type de {service_name}")


class {pascal_name}Create({pascal_name}Base):
    """Schéma pour la création d'un {service_name}"""
    # Ajoutez ici les champs spécifiques à la création
    pass


class {pascal_name}Update(BaseModel):
    """Schéma pour la mise à jour d'un {service_name}"""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    status: Optional[{pascal_name}Status] = None
    type: Optional[{pascal_name}Type] = None


class {pascal_name}Response({pascal_name}Base):
    """Schéma de réponse pour un {service_name}"""
    id: UUID = Field(..., description="ID unique")
    created_at: datetime = Field(..., description="Date de création")
    updated_at: Optional[datetime] = Field(None, description="Date de dernière modification")
    
    class Config:
        from_attributes = True


class {pascal_name}List(BaseModel):
    """Schéma pour une liste paginée de {service_name}"""
    items: list[{pascal_name}Response]
    total: int
    skip: int
    limit: int
'''
    
    with open(service_path / "schemas.py", "w", encoding="utf-8") as f:
        f.write(content)


def create_init_file(service_path: Path, service_name: str):
    """Créer le fichier __init__.py"""
    content = f'''"""
Package {to_title(service_name)}
"""

from app.services.{service_name} import router

__all__ = ["router"]
'''
    
    with open(service_path / "__init__.py", "w", encoding="utf-8") as f:
        f.write(content)


def create_tests_directory(service_path: Path, service_name: str):
    """Créer le dossier tests avec un fichier de test basique"""
    tests_path = service_path / "tests"
    tests_path.mkdir(exist_ok=True)
    
    pascal_name = to_pascal_case(service_name)
    
    # Créer __init__.py
    (tests_path / "__init__.py").touch()
    
    # Créer test_handlers.py
    test_content = f'''"""
Tests pour les handlers du service {to_title(service_name)}
"""

import pytest
from uuid import uuid4
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.{service_name}.schemas import {pascal_name}Create, {pascal_name}Update
from app.services.{service_name}.handlers import (
    create_{service_name},
    get_{service_name}_by_id,
    get_all_{service_name},
    update_{service_name},
    delete_{service_name}
)
from app.services.{service_name}.constants import {pascal_name}Status, {pascal_name}Type


@pytest.mark.asyncio
async def test_create_{service_name}(async_session: AsyncSession):
    """Test de création d'un {service_name}"""
    # TODO: Implémenter le test
    pass


@pytest.mark.asyncio
async def test_get_{service_name}_by_id(async_session: AsyncSession):
    """Test de récupération d'un {service_name} par ID"""
    # TODO: Implémenter le test
    pass


@pytest.mark.asyncio
async def test_get_all_{service_name}(async_session: AsyncSession):
    """Test de récupération de tous les {service_name}"""
    # TODO: Implémenter le test
    pass


@pytest.mark.asyncio
async def test_update_{service_name}(async_session: AsyncSession):
    """Test de mise à jour d'un {service_name}"""
    # TODO: Implémenter le test
    pass


@pytest.mark.asyncio
async def test_delete_{service_name}(async_session: AsyncSession):
    """Test de suppression d'un {service_name}"""
    # TODO: Implémenter le test
    pass
'''
    
    with open(tests_path / f"test_{service_name}.py", "w", encoding="utf-8") as f:
        f.write(test_content)


def create_readme_file(service_path: Path, service_name: str):
    """Créer un fichier README.md pour le service"""
    pascal_name = to_pascal_case(service_name)
    title = to_title(service_name)
    
    content = f'''# Service {title}

## Description

Ce service gère les opérations liées aux {service_name}.

## Structure

```
{service_name}/
├── __init__.py          # Point d'entrée du package
├── handlers.py          # Logique métier
├── constants.py         # Constantes et enums
├── router.py            # Routes FastAPI
├── schemas.py           # Schémas Pydantic
├── README.md            # Documentation
└── tests/              # Tests unitaires
    ├── __init__.py
    └── test_{service_name}.py
```

## Endpoints

### POST /{service_name}
Créer un nouveau {service_name}

### GET /{service_name}/{{id}}
Récupérer un {service_name} par ID

### GET /{service_name}
Lister tous les {service_name} (avec pagination)

### PUT /{service_name}/{{id}}
Mettre à jour un {service_name}

### DELETE /{service_name}/{{id}}
Supprimer un {service_name}

## Utilisation

```python
# Dans main.py
from app.services.{service_name} import router as {service_name}_router

app.include_router({service_name}_router.router)
```

## Tests

```bash
# Exécuter les tests
pytest app/services/{service_name}/tests/

# Avec couverture
pytest app/services/{service_name}/tests/ --cov=app/services/{service_name}
```

## TODO

- [ ] Implémenter la logique métier dans handlers.py
- [ ] Créer le modèle SQLAlchemy {pascal_name}
- [ ] Écrire les tests unitaires
- [ ] Ajouter la validation des données
- [ ] Documenter les cas d'usage

## Notes

Service généré automatiquement le {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
'''
    
    with open(service_path / "README.md", "w", encoding="utf-8") as f:
        f.write(content)


def generate_service(service_name: str, with_tests: bool = True):
    """
    Générer un nouveau service avec tous ses fichiers
    
    Args:
        service_name: Nom du service à créer
        with_tests: Si True, créer aussi le dossier tests
    """
    # Normaliser le nom du service
    service_name = to_snake_case(service_name)
    
    # Chemin du service
    service_path = Path("app/services") / service_name
    
    # Vérifier si le service existe déjà
    if service_path.exists():
        print(f"❌ Le service '{service_name}' existe déjà dans app/services/")
        sys.exit(1)
    
    # Créer le dossier du service
    service_path.mkdir(parents=True, exist_ok=True)
    print(f"📁 Création du dossier: {service_path}")
    
    # Créer les fichiers
    print("📝 Génération des fichiers...")
    
    create_handlers_file(service_path, service_name)
    print(f"  ✅ handlers.py")
    
    create_constants_file(service_path, service_name)
    print(f"  ✅ constants.py")
    
    create_router_file(service_path, service_name)
    print(f"  ✅ router.py")
    
    create_schemas_file(service_path, service_name)
    print(f"  ✅ schemas.py")
    
    create_init_file(service_path, service_name)
    print(f"  ✅ __init__.py")
    
    create_readme_file(service_path, service_name)
    print(f"  ✅ README.md")
    
    # Créer les tests si demandé
    if with_tests:
        create_tests_directory(service_path, service_name)
        print(f"  ✅ tests/")
    
    print(f"\n✨ Service '{service_name}' créé avec succès !")
    print(f"\n📍 Prochaines étapes:")
    print(f"   1. Créer le modèle dans app/common/models/{to_pascal_case(service_name)}.py")
    print(f"   2. Implémenter la logique dans app/services/{service_name}/handlers.py")
    print(f"   3. Ajouter le router dans main.py:")
    print(f"      from app.services.{service_name} import router as {service_name}_router")
    print(f"      app.include_router({service_name}_router.router)")
    print(f"   4. Écrire les tests dans app/services/{service_name}/tests/")


def main():
    """Point d'entrée du script"""
    if len(sys.argv) < 2:
        print("❌ Usage: python scaffold.py <nom_du_service> [--no-tests]")
        print("   Exemple: python scaffold.py products")
        print("   Exemple: python scaffold.py user-profiles --no-tests")
        sys.exit(1)
    
    service_name = sys.argv[1]
    with_tests = "--no-tests" not in sys.argv
    
    generate_service(service_name, with_tests)


if __name__ == "__main__":
    main()