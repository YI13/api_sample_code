from typing import Optional
from pydantic import BaseModel


class Parking(BaseModel):
    floor: str
    zone: str
    parking_number: str
    license_plate: Optional[str] = None
    is_available: Optional[bool] = None