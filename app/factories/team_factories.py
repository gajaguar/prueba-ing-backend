import factory

from app.models import Team


class RandomTeamFactory(factory.Factory):
    """
    Class representing a random team factory.
    Use random data to create random team.
    """
    class Meta:
        model = Team


    team_name = factory.Faker("word")
