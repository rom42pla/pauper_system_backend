from fastapi import APIRouter
from scripts import utils

router = APIRouter(
    prefix="/utils",
    tags=["utils"]
)


@router.get("/roll/{roll_string}")
async def roll_dice(roll_string: str):
    return utils.roll_dice(roll_string=roll_string)


