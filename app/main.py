import uvicorn

from fastapi import FastAPI

from app.database import init_db
from app.routers import *


app = FastAPI()

app.include_router(levels_router)
app.include_router(players_router)
app.include_router(schemes_router)
app.include_router(teams_router)

@app.on_event("startup")
def startup():
    """
    Initialize the database if this option is setted in environment variables.
    """
    init_db()

@app.get("/")
def root():
    """
    Welcome page.
    """
    return {"hello": "world"}
    
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=80)
