from pydantic import BaseModel, Field
from random import random, choice


def create_price():
    return round(random() * choice([10, 20, 50, 100, 500, 1000]), 2)


class GoodsIn(BaseModel):
    name: str = Field(..., max_length=32)
    description: str = Field(..., max_length=500)
    price: float = Field(..., gt=0.0)


class Goods(GoodsIn):
    id: int
