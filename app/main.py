from typing import Optional
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from sqlmodel import Field, SQLModel, Session, create_engine, select

# from pycaret.classification import *
# import pandas as pd
# import sqlite3 as sql
# from pandas_profiling import ProfileReport
# import numpy as np
# import uvicorn

class ResultBase(SQLModel):
    competence: float
    network_ability: float
    promoted: bool

class Result(ResultBase, table=True):
    __tablename__ = "data"

    id: Optional[int] = Field(default=None, primary_key=True)

class ResultRead(ResultBase):
    id: int

templates=Jinja2Templates(directory="templates")
DESCRIPTION = """
API for the Quick Algorithm's Streaming Pipeline challenge.
"""

app = FastAPI(
    title="QA Data Streaming Mock API",
    description=DESCRIPTION,
    version="0.0.2",
)
# @app.on_event
# async def start():
#     conn = sql.connect('sqlite:////data/main.db')
#     df1 = pd.read_sql_query("SELECT * FROM data LIMIT 1000", conn)

#     training= setup(data=df1, target='promoted',profile=True,log_profile=True)
#     model=create_model("ada")

#     model_ada=predict_model(model)
#     profile_ada=ProfileReport(model_ada)
#     profile_ada.to_file("templates/report.html")

#     cm=create_model('ada')
#     tuned_cm = tune_model(cm)
#     final_cm = finalize_model(tuned_cm)


@app.get("/", response_class=HTMLResponse)
async def home(request:Request):
    context={'request':request}
    return  templates.TemplateResponse("index_old.html",context)

@app.get('/api/v1/data', response_model=list[ResultRead])
def read_data(page: int):
    engine = create_engine('sqlite:////data/main.db')
    with Session(engine) as session:
        results = session.exec(
            select(Result).limit(10).offset(10*page)
        ).all()
    return results
