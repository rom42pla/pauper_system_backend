from fastapi import APIRouter, HTTPException, status

from models.misc import RollResult
from scripts import utils

router = APIRouter(
    prefix="/utils",
    tags=["utils"]
)


@router.get("/roll/{roll_string}", response_model=RollResult)
async def roll_dice(roll_string: str):
    try:
        steps = utils.roll_dice(roll_string=roll_string, return_steps=True)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Roll '{roll_string}' not understood. "
                                   f"Valid rolls are e.g. '2d20 + 5' or '2d20 - d4 - 1'")
    return RollResult(result=int(steps[-1]), steps=steps)


