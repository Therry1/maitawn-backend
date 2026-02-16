"""
Constantes pour le service Birth Management
"""

from enum import Enum


class BirthManagementStatus(str, Enum):
    """Statuts possibles pour birth_management"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
    ARCHIVED = "archived"


class BirthManagementType(str, Enum):
    """Types possibles pour birth_management"""
    TYPE_A = "type_a"
    TYPE_B = "type_b"
    TYPE_C = "type_c"


# Constantes de configuration
MAX_BIRTH_MANAGEMENT_PER_PAGE = 100
DEFAULT_BIRTH_MANAGEMENT_LIMIT = 20

# Messages d'erreur
ERROR_NOT_FOUND = "BirthManagement not found"
ERROR_ALREADY_EXISTS = "BirthManagement already exists"
ERROR_INVALID_STATUS = "Invalid birth_management status"
ERROR_UNAUTHORIZED = "Unauthorized to access this birth_management"

# Messages de succès
SUCCESS_CREATED = "BirthManagement created successfully"
SUCCESS_UPDATED = "BirthManagement updated successfully"
SUCCESS_DELETED = "BirthManagement deleted successfully"
