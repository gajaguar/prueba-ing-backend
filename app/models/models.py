from typing import List, Optional
from datetime import datetime

from sqlalchemy import Column, DateTime, sql, String
from sqlmodel import Field, Relationship, SQLModel


class Auditor(SQLModel):
    """
    Class containing the common attributes for all entities.
    """
    created_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=sql.func.now(),
        )
    )
    updated_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True),
            onupdate=sql.func.now(),
        )
    )


class Scheme(Auditor, table=True):
    """
    Class representing the scheme entity.
    """
    scheme_id: Optional[int] = Field(default=None, primary_key=True)
    scheme_name: str = Field(
        ...,
        sa_column=Column(
            "scheme_name",
            String(100),
            unique=True,
        )
    )
    levels: List["Level"] = Relationship(back_populates="scheme")


class Level(Auditor, table=True):
    """
    Class representing the level entity.
    """
    level_id: Optional[int] = Field(default=None, primary_key=True)
    scheme_id: Optional[int] = Field(default=1, foreign_key="scheme.scheme_id")
    level_name: str = Field(
        ...,
        sa_column=Column(
            "level_name",
            String(50),
            unique=True,
        )
    )
    level_goals: int = Field(..., ge=0)
    scheme: Optional["Scheme"] = Relationship(back_populates="levels")
    players: List["Player"] = Relationship(back_populates="level")


class Team(Auditor, table=True):
    """
    Class representing the team entity.
    """
    team_id: Optional[int] = Field(default=None, primary_key=True)
    team_name: str = Field(
        ...,
        sa_column=Column(
            "team_name",
            String(100),
            unique=True,
        )
    )
    players: List["Player"] = Relationship(back_populates="team")


class Player(Auditor, table=True):
    """
    Class representing the player entity.
    """
    player_id: Optional[int] = Field(default=None, primary_key=True)
    level_id: Optional[int] = Field(default=None, foreign_key="level.level_id")
    team_id: Optional[int] = Field(default=None, foreign_key="team.team_id")
    player_name: str = Field(
        ...,
        sa_column=Column(
            "player_name",
            String(100),
            unique=True,
        )
    )
    player_goals: int = Field(..., ge=0)
    player_base_salary: int = Field(..., gt=0)
    player_bonus_salary: int = Field(..., gt=0)
    player_integrated_salary: Optional[int] = Field(default=None)
    level: Optional["Level"] = Relationship(back_populates="players")
    team: Optional["Team"] = Relationship(back_populates="players")
