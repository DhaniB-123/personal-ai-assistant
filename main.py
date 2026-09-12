from fastapi import FastAPI
from routers import chat
import models
from database import base,engine
from fastapi.middleware.cors import CORSMiddleware

base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ai-ui-rouge.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)

