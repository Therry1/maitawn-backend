# Service Institution Management

## Description

Ce service gère les opérations liées aux institution_management.

## Structure

```
institution_management/
├── __init__.py          # Point d'entrée du package
├── handlers.py          # Logique métier
├── constants.py         # Constantes et enums
├── router.py            # Routes FastAPI
├── schemas.py           # Schémas Pydantic
├── README.md            # Documentation
└── tests/              # Tests unitaires
    ├── __init__.py
    └── test_institution_management.py
```

## Endpoints

### POST /institution_management
Créer un nouveau institution_management

### GET /institution_management/{id}
Récupérer un institution_management par ID

### GET /institution_management
Lister tous les institution_management (avec pagination)

### PUT /institution_management/{id}
Mettre à jour un institution_management

### DELETE /institution_management/{id}
Supprimer un institution_management

## Utilisation

```python
# Dans main.py
from app.services.institution_management import router as institution_management_router

app.include_router(institution_management_router.router)
```

## Tests

```bash
# Exécuter les tests
pytest app/services/institution_management/tests/

# Avec couverture
pytest app/services/institution_management/tests/ --cov=app/services/institution_management
```

## TODO

- [ ] Implémenter la logique métier dans handlers.py
- [ ] Créer le modèle SQLAlchemy InstitutionManagement
- [ ] Écrire les tests unitaires
- [ ] Ajouter la validation des données
- [ ] Documenter les cas d'usage

## Notes

Service généré automatiquement le 2026-02-21 06:25:28
