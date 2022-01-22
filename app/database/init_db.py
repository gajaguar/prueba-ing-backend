from app.core import settings
from app.database.reset import crate_all
from app.database.reset import drop_all


def init_db()->None:
    """
    Run the database initialization functions according to the settings.
    """
    if settings.DB_RESET == "true" or settings.DB_RESET == "True":
        drop_all()
        crate_all()
