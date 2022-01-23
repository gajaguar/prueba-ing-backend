from sqlmodel import Session

from app.models import Player
from app.resources.base_resource import BaseResource
from app.resources.teams_resource import teams
from app.responses import NotFoundException
from app.schemas import PlayerCreate, PlayerUpdate
from app.utils import calculate_bonus
from app.utils import evaluate_goals_ratio
from app.utils import insert_integrated_salary


class PlayersResource(BaseResource[Player, PlayerCreate, PlayerUpdate]):
    """
    Class representing a players resource.
    """
    def get_individual_goals_ratio(self, db: Session, id: int) -> float:
        """
        Obtain the individual goals ratio of a player.
        """
        player = db.get(self.model, id)
        if player == None:
            raise NotFoundException
        reached_goals = player.player_goals
        required_goals = player.level.level_goals
        individual_goals_ratio = evaluate_goals_ratio(
            reached_goals,
            required_goals,
        )
        return individual_goals_ratio

    def get_bonus_salary(self, db: Session, id: int) -> int:
        """
        Obtain the bonus salary of a player.
        """
        player = db.get(self.model, id)
        if player == None:
            raise NotFoundException
        individual_goals_ratio = self.get_individual_goals_ratio(db, id)
        team_goals_ratio = teams.get_team_goals_ratio(db, player.team_id)
        calculated_bonus = calculate_bonus(
            player.player_bonus_salary,
            individual_goals_ratio,
            team_goals_ratio,
        )
        return calculated_bonus

    def get_one(self, db: Session, id: int) -> Player:
        """
        Obtain a single player from the database and calculate its integrated
        salary.
        """
        player = db.get(self.model, id)
        if player == None:
            raise NotFoundException
        bonus_salary = self.get_bonus_salary(db, id)
        updated_player = insert_integrated_salary(player, bonus_salary)
        return updated_player
 

players = PlayersResource(Player)
