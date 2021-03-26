from typing import List, Optional

from pydantic import BaseModel


class RollResult(BaseModel):
    result: int
    steps: Optional[List[str]]
