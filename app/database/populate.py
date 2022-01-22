from app.factories import *
from app.resources import *


def populate_schemes(quantity: int)-> None:
    """
    Populate the database with specified quantity of schemes.
    """
    random_schemes = RandomSchemeFactory.create_batch(quantity)
    for scheme in random_schemes:
        schemes.create(scheme)
    print("DEBUG:   ", f"{quantity} random schemes created.")

def populate_levels(quantity: int)-> None:
    """
    Populate the database with specified quantity of levels.
    """
    random_levels = RandomLevelFactory.create_batch(quantity)
    for level in random_levels:
        levels.create(level)

def populate_teams(quantity: int)-> None:
    """
    Populate the database with specified quantity of teams.
    """
    random_teams = RandomTeamFactory.create_batch(quantity)
    for team in random_teams:
        teams.create(team)

def populate_players(quantity: int)-> None:
    """
    Populate the database with specified quantity of players.
    """
    random_players = RandomPlayerFactory.create_batch(quantity)
    for player in random_players:
        players.create(player)
