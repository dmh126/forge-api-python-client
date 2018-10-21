from .authentication import Authentication
from .formats import Formats
from .buckets import Buckets
from .hubs import Hubs
from .projects import Projects
from .folders import Folders
from .items import Items
from .objects import Objects

class ApiClient(
    Authentication,
    Buckets,
    Formats,
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
