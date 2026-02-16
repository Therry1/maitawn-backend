"""
Constantes pour le service Trash Management
"""

from enum import Enum


class TrashManagementStatus(str, Enum):
    """Statuts possibles pour trash_management"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
    ARCHIVED = "archived"


class TrashManagementType(str, Enum):
    """Types possibles pour trash_management"""
    TYPE_A = "type_a"
    TYPE_B = "type_b"
    TYPE_C = "type_c"


# Constantes de configuration
MAX_TRASH_MANAGEMENT_PER_PAGE = 100
DEFAULT_TRASH_MANAGEMENT_LIMIT = 20

# Messages d'erreur
ERROR_NOT_FOUND = "TrashManagement not found"
ERROR_ALREADY_EXISTS = "TrashManagement already exists"
ERROR_INVALID_STATUS = "Invalid trash_management status"
ERROR_UNAUTHORIZED = "Unauthorized to access this trash_management"

# Messages de succès
SUCCESS_CREATED = "TrashManagement created successfully"
SUCCESS_UPDATED = "TrashManagement updated successfully"
SUCCESS_DELETED = "TrashManagement deleted successfully"
