from sqlmodel import SQLModel

from app.database import engine
from app.models import *


def drop_all()->None:
    """
    Destroy complete database.
    """
    SQLModel.metadata.drop_all(engine)
    print("DATABASE:", "Database and tables dropped.")

def crate_all()->None:
    """
    Create database and all tables according to models.
    """
    SQLModel.metadata.create_all(engine)
    print("DATABASE:", "Database and tables created.")
