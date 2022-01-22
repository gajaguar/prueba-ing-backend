import factory

from app.core import settings
from app.models import Level


class RandomLevelFactory(factory.Factory):
    """
    Class representing a random level factory.
    Use random data to create random level.
    """
    class Meta:
        model = Level


    scheme_id = factory.Faker(
        "pyint",
        min_value=1,
        max_value=settings.DB_POPULATION
    )
    level_name = factory.Faker("word")
