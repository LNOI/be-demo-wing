from fastapi import FastAPI
from src.api.v1 import router_prompt
from src.core.middleware import LoggingMiddleware
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv()
# from src.db.base import *
app = FastAPI(
    title="FastAPI templates",
    version="0.1.0",
    description="This is template for example project FastAPI"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.middleware("http")(LoggingMiddleware())
app.include_router(router=router_prompt.router)
# def create_tables():
#     Base.metadata.create_all(bind=engine)

# if __name__ == "__main__":
#     pass
    # create_tables()
