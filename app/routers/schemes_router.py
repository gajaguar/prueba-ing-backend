from app.resources import schemes
from app.schemas import Scheme, SchemeCreate, SchemeUpdate
from app.routers.base_router import setup_router


schemes_router = setup_router(
    schemes,
    "schemes",
    Scheme,
    SchemeCreate,
    SchemeUpdate
)
