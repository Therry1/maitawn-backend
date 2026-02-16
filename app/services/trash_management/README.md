# Service Trash Management

## Description

Ce service gère les opérations liées aux trash_management.

## Structure

```
trash_management/
├── __init__.py          # Point d'entrée du package
├── handlers.py          # Logique métier
├── constants.py         # Constantes et enums
├── router.py            # Routes FastAPI
├── schemas.py           # Schémas Pydantic
├── README.md            # Documentation
└── tests/              # Tests unitaires
    ├── __init__.py
    └── test_trash_management.py
```

## Endpoints

### POST /trash_management
Créer un nouveau trash_management

### GET /trash_management/{id}
Récupérer un trash_management par ID

### GET /trash_management
Lister tous les trash_management (avec pagination)

### PUT /trash_management/{id}
Mettre à jour un trash_management

### DELETE /trash_management/{id}
Supprimer un trash_management

## Utilisation

```python
# Dans main.py
from app.services.trash_management import router as trash_management_router

app.include_router(trash_management_router.router)
```

## Tests

```bash
# Exécuter les tests
pytest app/services/trash_management/tests/

# Avec couverture
pytest app/services/trash_management/tests/ --cov=app/services/trash_management
```

## TODO

- [ ] Implémenter la logique métier dans handlers.py
- [ ] Créer le modèle SQLAlchemy TrashManagement
- [ ] Écrire les tests unitaires
- [ ] Ajouter la validation des données
- [ ] Documenter les cas d'usage

## Notes

Service généré automatiquement le 2026-02-16 01:40:06
