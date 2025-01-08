from fastapi import APIRouter
from fastapi import Form
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from app.core.calculations import ChemiCalculator

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.post("/", response_class=HTMLResponse)
def read_results(request: Request, formula: str = Form(...)):
    try:
        chimi_instance = ChemiCalculator(formula)
    except ValueError:
        context = {"request": request, "name": "ChemiCalc",
                   "validation_results": f"Invalid formula submitted: {formula}"}
        return templates.TemplateResponse("home.html", context)

    if not getattr(chimi_instance, 'element', None):  # Check if 'element' exists and is not None
        context = {"request": request, "name": "ChemiCalc",
                   "validation_results": f"Invalid formula submitted: {chimi_instance.unicode}"}
        return templates.TemplateResponse("home.html", context)

    molar_mass = f"Molar mass: {chimi_instance.formula_weight:.2f} g/mol"
    moles = f"Moles on 1000 grams: {chimi_instance.calculate_moles(1000)}"

    context = {"request": request, "name": "ChemiCalc",
               "formula_txt": chimi_instance.unicode,
               "molar_mass": molar_mass,
               "percentage_composition": chimi_instance.percentage_composition,
               "moles": moles,
               }

    return templates.TemplateResponse("calculate.html", context)
