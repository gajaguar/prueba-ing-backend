from app.models import Scheme
from app.resources.base_resource import BaseResource
from app.schemas import SchemeCreate, SchemeUpdate


class SchemesResource(BaseResource[Scheme, SchemeCreate, SchemeUpdate]):
    """
    Class representing a roles resource.
    """
    pass


schemes = SchemesResource(Scheme)
