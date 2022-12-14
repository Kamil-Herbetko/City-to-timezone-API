import uuid
from pydantic import BaseModel, Field


class CityToTimeZoneModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    city: str = Field(...)
    timezone: int = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                "city": "Warsaw",
                "timezone": 2,
            }
        }
