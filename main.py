import asyncio
import webbrowser

import uvicorn
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from app.api.results import router as results_router
from app.api.home import router as home_router

templates = Jinja2Templates(directory="app/templates")

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(home_router, tags=["home"])
app.include_router(results_router, prefix="/results", tags=["results"])

async def open_browser():
    webbrowser.open("http://127.0.0.1:9000/")

if __name__ == "__main__":
    asyncio.run(open_browser())
    uvicorn.run("main:app", host="127.0.0.1", port=9000, log_level="info", reload=True, workers=1)

