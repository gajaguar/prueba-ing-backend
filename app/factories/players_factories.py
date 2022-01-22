import factory

from app.core import settings
from app.models import Player


class RandomPlayerFactory(factory.Factory):
    """
    Class representing a random player factory.
    Use random data to create random player.
    """
    class Meta:
        model = Player


    level_id: int = factory.Faker(
        "pyint",
        min_value=1,
        max_value=settings.DB_POPULATION
    )
    team_id: int = factory.Faker(
        "pyint",
        min_value=1,
        max_value=settings.DB_POPULATION
    )
    player_name: str = factory.Faker("name")
    player_goals: int = factory.Faker("pyint", min_value=0, max_value=30)
    player_base_salary: int = factory.Faker(
        "pyint",
        min_value=1,
        max_value=10
    ) * 10000
    player_bonus_salary: int = factory.Faker(
        "pyint",
        min_value=1,
        max_value=10
    ) * 1000
