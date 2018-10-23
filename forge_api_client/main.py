"""
AUTHOR: Damian Harasymczuk, Contecht GMBH

CONTACT: harasymczuk@contecht.eu

LICENSE: MIT
"""

from .authentication import Authentication
from .derivatives import Derivatives
from .buckets import Buckets
from .hubs import Hubs
from .projects import Projects
from .folders import Folders
from .items import Items
from .objects import Objects
from .versions import Versions

class ApiClient(
    Authentication,
    Buckets,
    Derivatives,
    Hubs,
    Projects,
    Folders,
    Items,
    Objects
    ):

    def __init__(self):
        self.access_token = None
        self.token_type = None
        self.scope = None
