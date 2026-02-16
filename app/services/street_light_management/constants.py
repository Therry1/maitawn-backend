"""
Constantes pour le service Street Light Management
"""

from enum import Enum


class StreetLightManagementStatus(str, Enum):
    """Statuts possibles pour street_light_management"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
    ARCHIVED = "archived"


class StreetLightManagementType(str, Enum):
    """Types possibles pour street_light_management"""
    TYPE_A = "type_a"
    TYPE_B = "type_b"
    TYPE_C = "type_c"


# Constantes de configuration
MAX_STREET_LIGHT_MANAGEMENT_PER_PAGE = 100
DEFAULT_STREET_LIGHT_MANAGEMENT_LIMIT = 20

# Messages d'erreur
ERROR_NOT_FOUND = "StreetLightManagement not found"
ERROR_ALREADY_EXISTS = "StreetLightManagement already exists"
ERROR_INVALID_STATUS = "Invalid street_light_management status"
ERROR_UNAUTHORIZED = "Unauthorized to access this street_light_management"

# Messages de succès
SUCCESS_CREATED = "StreetLightManagement created successfully"
SUCCESS_UPDATED = "StreetLightManagement updated successfully"
SUCCESS_DELETED = "StreetLightManagement deleted successfully"
