from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    context = {"request": request, "name": "ChemiCalc",
               "validation_results": ""
               }
    return templates.TemplateResponse("home.html", context)
