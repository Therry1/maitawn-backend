"""
Constantes pour le service Institution Management
"""

from enum import Enum

class IntitutionCat (str , Enum):
    mairie = 1

class InstitutionManagementStatus(str, Enum):
    """Statuts possibles pour institution_management"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
    ARCHIVED = "archived"


class InstitutionManagementType(str, Enum):
    """Types possibles pour institution_management"""
    TYPE_A = "type_a"
    TYPE_B = "type_b"
    TYPE_C = "type_c"


# Constantes de configuration
MAX_INSTITUTION_MANAGEMENT_PER_PAGE = 100
DEFAULT_INSTITUTION_MANAGEMENT_LIMIT = 20

# Messages d'erreur
ERROR_NOT_FOUND = "InstitutionManagement not found"
ERROR_ALREADY_EXISTS = "InstitutionManagement already exists"
ERROR_INVALID_STATUS = "Invalid institution_management status"
ERROR_UNAUTHORIZED = "Unauthorized to access this institution_management"

# Messages de succès
SUCCESS_CREATED = "InstitutionManagement created successfully"
SUCCESS_UPDATED = "InstitutionManagement updated successfully"
SUCCESS_DELETED = "InstitutionManagement deleted successfully"


ADAMAOUA_DATA = [
    {
        "region": "Adamaoua",
        "departements": [
            {"name": "Vina", "arrondissements": ["Ngaoundéré", "Meiganga", "Mbe", "Nyambaka", "Martap", "Banyo"]},
            {"name": "Mayo-Banyo", "arrondissements": ["Banyo", "Bankim", "Demsa"]},
            {"name": "Djérem", "arrondissements": ["Tibati", "Ngaoundal", "Ngaoundéré II"]},
            {"name": "Faro-et-Déo", "arrondissements": ["Tignère", "Bourha", "Galim-Tignère"]},
            {"name": "Mbéré", "arrondissements": ["Meiganga", "Mbere", "Ngaoundal"]}
        ]
    },
    {
        "region": "Centre",
        "departements": [
            {"name": "Mfoundi", "arrondissements": ["Yaoundé I", "Yaoundé II", "Yaoundé III"]},
            {"name": "Lekié", "arrondissements": ["Monatele", "Ebéjè"]},
            {"name": "Nyong-et-Kelle", "arrondissements": ["Abong-Mbang", "Ayos"]}
        ]
    },
    {
        "region": "Littoral",
        "departements": [
            {"name": "Wouri", "arrondissements": ["Douala I", "Douala II", "Douala III"]},
            {"name": "Nkam", "arrondissements": ["Yabassi", "Nkondjock"]}
        ]
    },
    {
        "region": "Nord",
        "departements": [
            {"name": "Mayo-Louti", "arrondissements": ["Guider", "Figuil"]},
            {"name": "Mayo-Rey", "arrondissements": ["Tcholliré", "Madingring"]}
        ]
    },
    {
        "region": "Extreme-Nord",
        "departements": [
            {"name": "Logone-et-Chari", "arrondissements": ["Kousséri", "Mokolo"]},
            {"name": "Mayo-Tsanaga", "arrondissements": ["Mora", "Madingring"]},
            {"name": "Diamaré", "arrondissements": ["Maroua I", "Maroua II"]}
        ]
    },
    {
        "region": "Ouest",
        "departements": [
            {"name": "Mifi", "arrondissements": ["Bafoussam", "Bamougoum"]},
            {"name": "Haut-Nkam", "arrondissements": ["Bafang", "Batcham"]}
        ]
    },
    {
        "region": "Sud-Ouest",
        "departements": [
            {"name": "Fako", "arrondissements": ["Limbe", "Buea"]},
            {"name": "Manyu", "arrondissements": ["Mamfe", "Tinto"]}
        ]
    },
    {
        "region": "Nord-Ouest",
        "departements": [
            {"name": "Mezam", "arrondissements": ["Bamenda I", "Bamenda II"]},
            {"name": "Momo", "arrondissements": ["Mbengwi", "Batibo"]}
        ]
    },
    {
        "region": "Sud",
        "departements": [
            {"name": "Océan", "arrondissements": ["Kribi", "Lolodorf"]},
            {"name": "Mvila", "arrondissements": ["Ebolowa", "Biassa"]}
        ]
    },
    {
        "region": "Est",
        "departements": [
            {"name": "Haut-Nyong", "arrondissements": ["Abong-Mbang", "Messamena"]},
            {"name": "Kadey", "arrondissements": ["Batouri", "Kette"]},
            {"name": "Boumba-et-Ngoko", "arrondissements": ["Moloundou", "Gari-Gombo"]}
        ]
    }
]

