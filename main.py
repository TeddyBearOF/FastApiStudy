from fastapi import FastAPI, Query
from typing import Optional
import uvicorn
from datetime import date
app = FastAPI()


@app.get("/hotels", summary="Main router", tags=["Master routers"])
def get_hotels(
        location: str,
        date_from: date,
        date_to: date,
        stars: Optional[int] = Query(None, ge=1, le=5),
        has_spa: Optional[bool] = False,
):
    return date_from, date_to


if __name__ == "__main__":
    uvicorn.run("main:app", reload = True)