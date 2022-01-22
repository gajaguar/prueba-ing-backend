from app.resources import players
from app.schemas import Player, PlayerCreate, PlayerUpdate
from app.routers.base_router import setup_router


players_router = setup_router(
    players,
    "players",
    Player,
    PlayerCreate,
    PlayerUpdate
)
