from typing import List, Optional

from pydantic import BaseModel, Field


class PlayerBase(BaseModel):
    """
    Class containing the base attributes of a player.
    """
    level_id: int = Field(
        ...,
        gt=0,
        title="Level ID",
        description="Indicate the skill level of the player.",
        example=1,
    )
    team_id: int = Field(
        ...,
        gt=0,
        title="Team ID",
        description="The team which players belongs to.",
        example=1,
    )
    player_name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        title="Player Name",
        description="When someone ask you 'What's your name'...",
        example="John Doe",
    )
    player_goals: int = Field(
        ...,
        ge=0,
        title="Player Goals",
        description="The number of goals scored by the player.",
        example=10,
    )
    player_base_salary: int = Field(
        ...,
        gt=0,
        title="Player Base Salary",
        description="The base salary of the player.",
        example=50000,
    )
    player_bonus_salary: int = Field(
        ...,
        gt=0,
        title="Player Bonus Salary",
        description="The bonus salary of the player.",
        example=10000,
    )
        

class PlayerCreate(PlayerBase):
    """
    Class containing properties to create a new player.
    """
    pass


class PlayerCreateBatch(BaseModel):
    """
    Class containing properties to create a new player.
    """
    players: List[PlayerCreate] = Field(...)


class PlayerUpdate(PlayerBase):
    """
    Class containing properties to update an existing user.
    """
    level_id: Optional[int] = Field(
        gt=0,
        title="Level ID",
        description="Indicate the skill level of the player.",
        example=1,
    )
    team_id: Optional[int] = Field(
        gt=0,
        title="Team ID",
        description="The team which players belongs to.",
        example=1,
    )
    player_name: Optional[str] = Field(
        min_length=1,
        max_length=100,
        title="Player Name",
        description="When someone ask you 'What's your name'...",
        example="John Doe",
    )
    player_goals: Optional[int] = Field(
        ge=0,
        title="Player Goals",
        description="The number of goals scored by the player.",
        example=10,
    )
    player_base_salary: Optional[int] = Field(
        gt=0,
        title="Player Base Salary",
        description="The base salary of the player.",
        example=50000,
    )
    player_bonus_salary: Optional[int] = Field(
        gt=0,
        title="Player Bonus Salary",
        description="The bonus salary of the player.",
        example=10000,
    )


class Player(PlayerBase):
    """
    Class containing properties to retrive a player to client.
    """
    player_id: int = Field(
        ...,
        gt=0,
        title="Player ID",
        description="Unique identifier of the user.",
        example=1,
    )
    player_integrated_salary: Optional[int] = Field(
        ...,
        gt=0,
        title="Player Integrated Salary",
        description="A calculation based on the base salary and bonus salary.",
        example=60000,
    )
