import factory

from app.models import Scheme


class RandomSchemeFactory(factory.Factory):
    """
    Class representing a random scheme factory.
    Use random data to create random scheme.
    """
    class Meta:
        model = Scheme


    scheme_name = factory.Faker("word")
