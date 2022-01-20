from app.models import Player
from app.resources.base_resource import BaseResource
from app.schemas import PlayerCreate, PlayerUpdate


class PlayersResource(BaseResource[Player, PlayerCreate, PlayerUpdate]):
    """
    Class representing a roles resource.
    """
    pass


players = PlayersResource(Player)
