from typing import List, Type, TypeVar

from fastapi import APIRouter, Depends, status
from pydantic import BaseModel
from sqlmodel import Session

from app.dependencies import get_session
from app.resources import BaseResource


ResourceType = TypeVar("ResourceType", bound=BaseResource)
SingleSchemaType = TypeVar("SingleSchemaType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

def setup_router(
    resource: Type[ResourceType],
    resource_name: str,
    single_schema: Type[SingleSchemaType],
    create_schema: Type[CreateSchemaType],
    update_schema: Type[UpdateSchemaType],
) -> APIRouter:
    """
    Set up a router for a given resource by adding basic CRUD paths.
    """
    router = APIRouter(
        prefix=f"/api/{resource_name}",
        tags=[f"{resource_name}"],
    )

    @router.post(
        "/",
        status_code=status.HTTP_201_CREATED,
        response_model=single_schema,
    )
    async def create_resource(
        data: create_schema,
        session: Session = Depends(get_session),
    ):
        """
        Create a new resource with requested data.
        """
        created = resource.create(session, data)
        return created

    @router.get(
        "/",
        status_code=status.HTTP_200_OK,
        response_model=List[single_schema],
    )
    async def read_resources(
        session: Session = Depends(get_session),
    ):
        """
        Retrieve all requested resources.
        """
        all = resource.get_all(session)
        return all

    @router.get(
        "/{id}",
        status_code=status.HTTP_200_OK,
        response_model=single_schema,
    )
    async def read_resource(
        id: int,
        session: Session = Depends(get_session),
    ):
        """
        Retrieve an specific resource.
        """
        obtained = resource.get_one(session, id)
        return obtained

    @router.patch(
        "/{id}",
        status_code=status.HTTP_200_OK,
        response_model=single_schema,
    )
    async def update_resource(
        id: int,
        data: update_schema,
        session: Session = Depends(get_session),
    ):
        """
        Update an specific resource with requested data.
        """
        updated = resource.update(session, id, data)
        return updated

    @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
    async def delete_resource(
        id: int,
        session: Session = Depends(get_session),
    ):
        """
        Erase an specific resource.
        """
        resource.delete(session, id)
        return None

    return router
