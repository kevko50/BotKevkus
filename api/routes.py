from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def home():
    return {"message": "BotKevkus API aktiv"}