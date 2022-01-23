from typing import Optional

from pydantic import BaseModel, Field


class TeamBase(BaseModel):
    """
    Class containing the base attributes of a team.
    """
    team_name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        title="Team Name",
        description="Name of the team",
        example="Resuelve FC",
    )


class TeamCreate(TeamBase):
    """
    Class containing properties to create a new team.
    """
    pass


class TeamUpdate(BaseModel):
    """
    Class containing properties to update an existing team.
    """
    team_name: Optional[str] = Field(
        min_length=1,
        max_length=100,
        title="Team Name",
        description="Name of the team",
        example="Resuelve FC",
    )


class Team(TeamBase):
    """
    Class containing properties to retrieve a team to the client.
    """
    team_id: int = Field(
        ...,
        gt=0,
        title="Team ID",
        description="Unique identifier of the team.",
        example=1,
    )
