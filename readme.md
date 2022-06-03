# Diabetes Predictor
![python 3.10.4](https://img.shields.io/badge/Python-3.10.4-blue.svg)
![html](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![numpy](https://img.shields.io/badge/Numpy-777BB4?logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/Pandas-2C2D72?logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit_learn-0078D4?logo=scikit-learn&logoColor=white)
![fastapi](https://img.shields.io/badge/fastapi-109989?logo=FASTAPI&logoColor=white)
![heroku](https://img.shields.io/badge/Heroku-430098?logo=heroku&logoColor=white)
![jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?logo=Jupyter&logoColor=white)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Diabetes Predictor App used to predict whether a person has diabetes or not based on certain input parameters created using python's scikit-learn, fastapi, numpy and joblib packages.

## Dataset Description

The datasets consist of several medical predictor (independent) variables and one target (dependent) variable, Outcome. Independent variables include the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.

The data contains the following columns:

| Feature Name               | Feature Description                                                                                 |
| -------------------------- | --------------------------------------------------------------------------------------------------- |
| Pregnancies                | Number of times pregnant                                                                            |
| Glucose                    | Plasma glucose concentration a 2 hours in an oral glucose tolerance test                            |
| BloodPressure              | Diastolic blood pressure (mm Hg)                                                                    |
| SkinThickness              | Triceps skin fold thickness (mm)                                                                    |
| Insulin                    | 2-Hour serum insulin (mu U/ml)                                                                      |
| BMI                        | Body mass index (weight in kg/(height in m)^2)                                                      |
| Diabetes pedigree function | Diabetes pedigree function (a function which scores likelihood of diabetes based on family history) |
| Age                        | Age (years)                                                                                         |
| Outcome                    | Class variable (0 or 1) 268 of 768 are 1, the others are 0                                          |

## Installation

Open Anaconda prompt and create new environment

```
conda create -n your_env_name python = (any_version_number)
```

Then Activate the newly created environment

```
conda activate your_env_name
```

Clone the repository using `git`

```
git clone https://github.com/Prakashdeveloper03/Diabetes-Predictor.git
```

Change to the cloned directory

```
cd <directory_name>
```

To install all requirement packages for the app

```
pip install -r requirements.txt
```

Then, Run the app

```
uvicorn main:app --reload
```

## 📷 Screenshots

### Home page

![app interface](markdown/home.png)

### Swagger UI

![swagger UI](markdown/swagger.png)

### Redoc UI

![redoc UI](markdown/redoc.png)

### Demo GIF

![demo gif](markdown/demo.gif)
