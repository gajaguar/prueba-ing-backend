from sqlmodel import Session

from app.models import Team
from app.resources.base_resource import BaseResource
from app.responses import NotFoundException
from app.schemas import TeamCreate, TeamUpdate
from app.utils import evaluate_goals_ratio


class TeamsResource(BaseResource[Team, TeamCreate, TeamUpdate]):
    """
    Class representing a teams resource.
    """
    def get_team_goals_ratio(self, db: Session, id: int) -> float:
        """
        Obtain the team goals ratio of a team.
        """
        team = db.get(self.model, id)
        if team == None:
            raise NotFoundException
        reached_goals = 0
        required_goals = 0
        players = team.players
        for player in players:
            reached_goals += player.player_goals
            required_goals += player.level.level_goals
        team_goals_ratio = evaluate_goals_ratio(
            reached_goals,
            required_goals,
        )
        return team_goals_ratio


teams = TeamsResource(Team)
