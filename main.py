"""
Main app file
"""
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field

# Создание приложения
app = FastAPI(
    title="Trading App"
)

# тестовая бд с пользователями
fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"}
]


class User(BaseModel):
    """User-model for validating data

    Args:
        BaseModel (pydentic): pydentic base model
    """
    id: int
    role: str
    name: str


# получение пользователя по id
@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]


# тестовая бд с трейдерами
fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC",
     "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC",
     "side": "sell", "price": 125, "amount": 2.12},
]


# модель данных "Сделка"
class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)  # огрничение длины строки
    side: str
    price: float = Field(ge=0)  # задется ограничение для ввода (>=0)
    amount: float


# добавление трейдера в бд
@app.post("/trades")
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}
