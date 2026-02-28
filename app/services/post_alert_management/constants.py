"""
Constantes pour le service Post Alert Management
"""

from enum import Enum

class ValidationState(int , Enum):
    accepted = 1
    pending = 0
    rejected = -1
    archived = 2