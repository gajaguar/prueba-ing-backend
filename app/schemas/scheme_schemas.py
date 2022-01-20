from typing import Optional

from pydantic import BaseModel, Field


class SchemeBase(BaseModel):
    """
    Class containing the base attributes of a scheme.
    """
    scheme_name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        title="Scheme Name",
        description="Name of the scheme",
        example="Resuelve FC",
    )


class SchemeCreate(SchemeBase):
    """
    Class containing properties to create a new scheme.
    """
    pass


class SchemeUpdate(BaseModel):
    """
    Class containing properties to update an existing scheme.
    """
    scheme_name: Optional[str] = Field(
        min_length=1,
        max_length=100,
        title="Scheme Name",
        description="Name of the scheme",
        example="Resuelve FC",
    )


class Scheme(SchemeBase):
    """
    Class containing properties to retrieve a scheme to the client.
    """
    scheme: int = Field(
        ...,
        gt=0,
        title="Scheme ID",
        description="Unique identifier of the scheme.",
        example=1,
    )
