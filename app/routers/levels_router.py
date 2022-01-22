from app.resources import levels
from app.schemas import Level, LevelCreate, LevelUpdate
from app.routers.base_router import setup_router


levels_router = setup_router(
    levels,
    "levels",
    Level,
    LevelCreate,
    LevelUpdate
)
