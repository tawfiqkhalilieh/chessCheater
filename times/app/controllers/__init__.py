from fastapi import APIRouter
from app.controllers.times.get_move import router as get_move_router

router = APIRouter()
router.include_router(get_move_router)