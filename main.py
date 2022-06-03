import joblib  # for loading model pickle file
import numpy as np  # for array conversion
import pandas as pd  # for data analysis

# FastAPI is a modern, fast (high-performance), web framework for building APIs with Python
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()  # instance of FastAPI class

# mount static folder files to /static route
app.mount("/static", StaticFiles(directory="static"), name="static")

# loads the ML model
model = joblib.load(open("models/model.pkl", "rb"))

# sets the templates folder for the app
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    """
    Function to render base.html at route '/' as a get request

    Args:
        request (Request): request in path operation that will return a template

    Returns:
        TemplateResponse: render base.html
    """
    return templates.TemplateResponse("base.html", {"request": request})


@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    pregnancies: int = Form(...),
    glucose: int = Form(...),
    bloodpressure: int = Form(...),
    skinthickness: int = Form(...),
    insulin: int = Form(...),
    bmi: float = Form(...),
    dpf: float = Form(...),
    age: int = Form(...),
):
    """
    Function to predict diabetes classification
    and shows the result by rendering result.html at route '/predict'

    Args:
        request (Request): request in path operation that will return a template
        pregnancies (int, optional): Pregnancies value
        glucose (int, optional): Glucose level
        bloodpressure (int, optional): Blood pressure level
        skinthickness (int, optional): Skinthickness value
        insulin (int, optional): Insulin level
        bmi (float, optional): Body mass index value
        dpf (float, optional): Diabetes pedigree function
        age (int, optional): Age value as int

    Returns:
        TemplateResponse: render result.html
    """
    data = pd.DataFrame(
        [[pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, dpf, age]],
        columns=[
            "Pregnancies",
            "Glucose",
            "BloodPressure",
            "SkinThickness",
            "Insulin",
            "BMI",
            "DPF",
            "Age",
        ],
    )  # input data as a dataframe
    prediction = model.predict(data)  # prediction using ML model
    return templates.TemplateResponse(
        "result.html", context={"prediction": prediction, "request": request}
    )
