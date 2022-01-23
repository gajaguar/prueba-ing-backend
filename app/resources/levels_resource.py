from app.models import Level
from app.resources.base_resource import BaseResource
from app.schemas import LevelCreate, LevelUpdate


class LevelsResource(BaseResource[Level, LevelCreate, LevelUpdate]):
    """
    Class representing a levels resource.
    """
    pass


levels = LevelsResource(Level)
