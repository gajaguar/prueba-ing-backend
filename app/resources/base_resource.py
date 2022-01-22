from typing import Generic, List, Optional, Type, TypeVar, Union

from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from sqlmodel import select, Session

from app.models import Auditor
from app.responses import NotFoundException
from app.responses import UniqueConstraintException
from app.utils import to_dict


ModelType = TypeVar("ModelType", bound=Auditor)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseResource(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
    Class representing a base resource.
    Set up basic CRUD operations:
    - create
    - read (one and all)
    - update
    - delete
    """
    def __init__(self, model: Type[ModelType]):
        """
        Create a new instace of `BaseResource` class.
        """
        self.model = model

    def create(
        self,
        db: Session,
        data: Union[CreateSchemaType, dict]
    ) -> ModelType:
        """
        Insert a new resource into the database.
        """
        obj_in_data = to_dict(data)
        resource = self.model(**obj_in_data)
        db.add(resource)
        try:
            db.commit()
        except IntegrityError:
            raise UniqueConstraintException()
        db.refresh(resource)
        return resource

    def get_one(self, db: Session, id: int) -> ModelType:
        """
        Obtain a single resource from the database.
        """
        resource = db.get(self.model, id)
        if resource == None:
            raise NotFoundException
        return resource
 
    def get_all(self, db: Session) -> List[ModelType]:
        """
        Obtain all resources from the database.
        """
        statement = select(self.model)
        result = db.exec(statement)
        users = result.all()
        return users

    def update(
        self,
        db: Session,
        id: int,
        data: Union[CreateSchemaType, dict]
    ) -> ModelType:
        """
        Update an existing resource in the database.
        """
        obj_in_data = to_dict(data)
        resource = db.get(self.model, id)
        if resource == None:
            raise NotFoundException
        for key, value in obj_in_data.items():
            setattr(resource, key, value)
        db.add(resource)
        try:
            db.commit()
        except IntegrityError as e:
            raise UniqueConstraintException(e.params[0])
        db.refresh(resource)
        return resource

    def delete(self, db: Session, id: int) -> bool:
        """
        Remove an existing resource from the database.
        """
        resource = db.get(self.model, id)
        if resource == None:
            raise NotFoundException
        db.delete(resource)
        db.commit()
        return True
