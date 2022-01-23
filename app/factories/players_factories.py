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


    level_id = factory.Faker(
        "random_int",
        min=1,
        max=settings.DB_POPULATION
    )
    team_id = factory.Faker(
        "random_int",
        min=1,
        max=settings.DB_POPULATION
    )
    player_name = factory.Faker("name")
    player_goals = factory.Faker("random_int", min=0, max=30)
    player_base_salary = factory.Faker("random_int", min=10000, max=100000)
    player_bonus_salary = factory.Faker("random_int", min=1000, max=10000)
