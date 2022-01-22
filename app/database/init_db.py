from app.core import settings
from app.database.populate import populate_schemes
from app.database.populate import populate_levels
from app.database.populate import populate_teams
from app.database.populate import populate_players
from app.database.reset import crate_all
from app.database.reset import drop_all


def init_db()->None:
    """
    Run the database initialization functions according to the settings.
    """
    if settings.DB_RESET == "true" or settings.DB_RESET == "True":
        drop_all()
        crate_all()
    if settings.DB_POPULATE == "true" or settings.DB_POPULATE == "True":
        populate_schemes(settings.DB_POPULATION) 
        populate_levels(settings.DB_POPULATION) 
        populate_teams(settings.DB_POPULATION) 
        populate_players(settings.DB_POPULATION) 
