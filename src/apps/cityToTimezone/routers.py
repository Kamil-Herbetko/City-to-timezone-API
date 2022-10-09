from fastapi import APIRouter, Body, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from .models import CityToTimeZoneModel

router = APIRouter()


@router.get("/{city}", response_description="Timezone for a given city")
async def get_timezone_for_given_city(request: Request, city: str):
    if (timezone := await request.app.mongodb["cityToTimezone"]):
        
