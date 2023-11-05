import os

import uvicorn
from fastapi import FastAPI
from sqlmodel import SQLModel
from starlette.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from session.db_session import engine

load_dotenv()  # take environment variables from .env.

import libro_biblioteca.libro_biblioteca_api


app = FastAPI(
    title="App ejemplo docs!",
    description="Project",
    summary="Deadpool's favorite app. Nuff said.",
    version="1.0.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=[
        libro_biblioteca.libro_biblioteca_api.tag_libro_biblioteca
    ],
)

app.include_router(libro_biblioteca.libro_biblioteca_api.router)

cors_origins_text = os.getenv('CORS_ORIGINS')
origins = cors_origins_text.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.get("/")
def index():
    """Return a friendly welcome message"""
    return {'message': 'Welcome!'}



if __name__ == "__main__":
    uvicorn.run("app_ejemplo:app", reload=True)