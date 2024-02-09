from pydantic import BaseModel, Field
from datetime import datetime


class OrderIn(BaseModel):
    user_id: int = Field(..., ge=1)
    goods_id: int = Field(..., ge=1)
    orderdate: datetime


class Order(OrderIn):
    id: int
