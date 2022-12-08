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

    __Args__:
        - __request (Request)__: request in path operation that will return a template

    __Returns__:
        - __TemplateResponse__: render `base.html`
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
    - __request (Request)__: request in path operation that will return a template
    - __pregnancies (int)__: Pregnancies value
    - __glucose (int)__: Glucose level
    - __bloodpressure (int)__: Blood pressure level
    - __skinthickness (int)__: Skinthickness value
    - __insulin (int)__: Insulin level
    - __bmi (float)__: Body mass index value
    - __dpf (float)__: Diabetes pedigree function
    - __age (int)__: Age value as int

    Returns:
    - __TemplateResponse__: render `result.html`
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
