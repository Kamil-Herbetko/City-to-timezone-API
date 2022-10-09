from fastapi import FastAPI
import uvicorn
from motor.motor_asyncio import AsyncIOMotorClient
from settings import settings

from apps.cityToTimezone.routers import router as cttt_router

app = FastAPI()


@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(
        settings.DB_URI,
        tls=True,
        tlsCertificateKeyFile=settings.DB_CERTIFICATE_PATH
    )
    app.mongodb = app.mongodb_client[settings.DB_NAME]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(cttt_router, tags=["cityToTimezone"], prefix="/cityToTimezone")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )
