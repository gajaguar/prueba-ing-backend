from app.resources import teams
from app.schemas import Team, TeamCreate, TeamUpdate
from app.routers.base_router import setup_router


teams_router = setup_router(
    teams,
    "teams",
    Team,
    TeamCreate,
    TeamUpdate
)
