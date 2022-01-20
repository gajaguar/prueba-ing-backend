from app.models import Team
from app.resources.base_resource import BaseResource
from app.schemas import TeamCreate, TeamUpdate


class TeamsResource(BaseResource[Team, TeamCreate, TeamUpdate]):
    """
    Class representing a roles resource.
    """
    pass


teams = TeamsResource(Team)
