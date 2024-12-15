# file orders/api/schemas.py
from enum import Enum
from typing import List, Optional
from uuid import UUID
from pydantic import conint, conlist, BaseModel, Field, field_validator
from datetime import datetime

class Size(Enum)
    small = 'small'
    medium = 'medium'
    big = 'big'

class Status(Enum)
    created = 'created'
    progress = 'progress'
    cancelled = 'cancelled'
    dispatched = 'dispatched'
    delivered = 'delivered'

class OrderItemSchema(BaseModel)
    product: str
    size: Size
    # optional type given as int, fields first argument specifies 1
    # second argument greater than or equal
    # third argument strictly integer 1, no string or float
    quantity: Optional[int] = Field(1,ge=1,strict=True)
    # additional validator in order to restrain from using the null value
    @field_validator('quantity')
    def quantity_not_nullable(cls, value):
        if value is None:
            raise ValueError('quantity may not be none')
        return value

class CreateOrderSchema(BaseModel):
    orders: List[GetOrderSchema]