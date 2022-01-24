from typing import List

from fastapi import Depends, status
from sqlmodel import Session

from app.dependencies import get_session
from app.resources import players
from app.routers.base_router import setup_router
from app.schemas import Player
from app.schemas import PlayerCreate
from app.schemas import PlayerCreateBatch
from app.schemas import PlayerUpdate


players_router = setup_router(
    players,
    "players",
    Player,
    PlayerCreate,
    PlayerUpdate
)

@players_router.post(
    "/batch",
    status_code=status.HTTP_201_CREATED,
    response_model=List[Player],
)
async def create_players(
    data: PlayerCreateBatch,
    session: Session = Depends(get_session),
):
    """
    Create multiple players in the database.
    """
    created = players.create_by_batch(session, data)
    return created
