from sqlmodel import Session

from app.database import engine
from app.factories import *
from app.resources import *


def populate_schemes(quantity: int)-> None:
    """
    Populate the database with specified quantity of schemes.
    """
    session = Session(engine)
    random_schemes = RandomSchemeFactory.create_batch(quantity)
    for scheme in random_schemes:
        schemes.create(session, scheme)
    print("DATABASE:", f"{quantity} random schemes created.")

def populate_levels(quantity: int)-> None:
    """
    Populate the database with specified quantity of levels.
    """
    session = Session(engine)
    random_levels = RandomLevelFactory.create_batch(quantity)
    for level in random_levels:
        levels.create(session, level)
    print("DATABASE:", f"{quantity} random levels created.")

def populate_teams(quantity: int)-> None:
    """
    Populate the database with specified quantity of teams.
    """
    session = Session(engine)
    random_teams = RandomTeamFactory.create_batch(quantity)
    for team in random_teams:
        teams.create(session, team)
    print("DATABASE:", f"{quantity} random teams created.")

def populate_players(quantity: int)-> None:
    """
    Populate the database with specified quantity of players.
    """
    session = Session(engine)
    random_players = RandomPlayerFactory.create_batch(quantity)
    for player in random_players:
        players.create(session, player)
    print("DATABASE:", f"{quantity} random players created.")
