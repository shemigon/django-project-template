from .django import *

try:
    from . import local
except ImportError as e:
    pass
