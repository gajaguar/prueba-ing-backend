from typing import Optional

from pydantic import BaseModel, Field


class LevelBase(BaseModel):
    """
    Class containing the base attributes of a level.
    """
    scheme_id: int = Field(
        ...,
        gt=0,
        title="Scheme ID",
        description="Refer to the goals requirement scheme.",
        example=1,
    )
    level_name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        title="Level Name",
        description="Name of the level",
        example="Cuauh",
    )
    level_goals: int = Field(
        ...,
        ge=0,
        title="Level Goals",
        description="Minimum of goals required to reach the complete bonus",
    )


class LevelCreate(LevelBase):
    """
    Class containing properties to create a new level.
    """
    pass


class LevelUpdate(LevelBase):
    """
    Class containing properties to update an existing level.
    """
    scheme_id: Optional[int] = Field(
        gt=0,
        title="Scheme ID",
        description="Refer to the goals requirement scheme.",
        example=1,
    )
    level_name: Optional[str] = Field(
        min_length=1,
        max_length=100,
        title="Level Name",
        description="Name of the level",
        example="Cuauh",
    )
    level_goals: Optional[int] = Field(
        ge=0,
        title="Level Goals",
        description="Minimum of goals required to reach the complete bonus",
    )


class Level(LevelBase):
    """
    Class containing properties to retrieve a level to the client.
    """
    level_id: int = Field(
        ...,
        title="Level ID",
        description="Unique identifier of the level.",
        example=1,
    )
