import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

logger = logging.getLogger("app_logger")
logger.info("session starts.")

origins = ["*"]
api_version = "apiv1"
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    pass
    logger.info("startup started")
    logger.info("startup fisnihed successfully")

@app.on_event("shutdown")
def shutdown_event():
    logger.info("shutdown fisnihed successfully")

@app.get("/api/hello")
def hello_world():
    msg = {
        "status": 200,
        "message": "Hello world!"
    }
    return msg

class APPTaker:
    app: FastAPI = app