from sqlmodel import create_engine

from app.database.connection import get_uri


uri = get_uri()
"""
Uri string for the database engine.
"""

engine = create_engine(uri)
"""
SQLModel database engine.
"""
