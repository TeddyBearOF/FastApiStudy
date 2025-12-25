from fastapi import FastAPI, Query, Depends
from typing import Optional
import uvicorn
from datetime import date
from pydantic import BaseModel

app = FastAPI()


#Чтобы не передавать кучу аргументов в get-запросе
class HotelsSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        stars: Optional[int] = Query(None, ge=1, le=5),
        has_spa: Optional[bool] = False
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa


#pydantic-схема
#Отвечает за request body
#Request Body — тело запроса (тело сообщения) в HTTP-запросах.
#Это часть сообщения, в которой передаются данные от клиента на сервер.
class SHotel(BaseModel):
    address: str
    name: str
    stars: int


#router, он же "ручка", за которую дёргают для выполнения действий
@app.get(
    "/hotels",
    summary="Main router",
    tags=["Master routers"]
)

def get_hotels(
        search_args: HotelsSearchArgs = Depends()
) -> list[SHotel]:
    hotels = [
        {
            "address": "Улица Пушкина",
            "name": "Super Hotel",
            "stars": 5
        }
    ]
    return hotels


#Тоже pydantic-схема
class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


#router
@app.post("/bookings")
def add_booking(booking: SBooking):
    pass

