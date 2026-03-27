"""
xval - Xval's Python SDK
"""

import importlib.metadata

VERSION = "v0.1.2"
__version__ = VERSION

from .xval import (
    run,
    template,
    TEMPLATE_LIST,
)

__all__ = [
    'run',
    'template',
    'TEMPLATE_LIST',
    'VERSION',
]


 
