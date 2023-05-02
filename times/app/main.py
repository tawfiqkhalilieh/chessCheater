from fastapi import FastAPI
from config import settings
from app.models.game import Game
from app.services.utils.validate_game_url import validate_url as validate_game_url
from app.services.times.get_move import get_move as get_move_crud
from app.services.times.add_move import add_move as add_move_curd
from fastapi import HTTPException
from app.database.table import table
from typing import Optional
from app.services.learn import learn_game
from selenium import webdriver

app = FastAPI()

@app.get(f"/health", description="Health check route")
def health_check():
    return "I am okay, thank you for asking"


@app.get("/", description="root route of the service")
def root():
    return settings.app_name
    
@app.get(path="/get/{move}/{color}")
def get_move(move: Optional[int], color: Optional[str]):
    try:
        return get_move_crud(move=move,color=color)
    except HTTPException as e:
        raise HTTPException(status_code=401, detail=e)
    
@app.post(path="/add/{move}/{color}/{value}")
def add_move(move: int, color: str, value: float):
    try:
        return add_move_curd(move=move, color=color, value=value)
    except HTTPException as e:
        raise HTTPException(status_code=401, detail=e)

@app.on_event("startup")
async def stratup_table():
    table.create_tables()