from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RestaurantBase(BaseModel):
    name: str
    description: Optional[str] = None
    cuisine_type: str
    address: str
    phone: Optional[str] = None
    price_range: str
    delivery_time: int
    delivery_fee: float = 0.0
    image_url: Optional[str] = None

class RestaurantCreate(RestaurantBase):
    pass

class RestaurantResponse(RestaurantBase):
    id: int
    rating: float
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True