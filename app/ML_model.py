import pandas as pd
import sqlite3 as sql
from pandas_profiling import ProfileReport
import numpy as np
from pycaret.classification import *


def find_best_ml(path='sqlite:////data/main.db', batch_size=1000):
    conn = sql.connect(path)
    df1 = pd.read_sql_query(f"SELECT * FROM data LIMIT {batch_size}", conn)

    training= setup(data=df1, target='promoted',profile=True,log_profile=True)
    best_approx= compare_models()

    predict_model(best_approx)

    best_model=save_model(best_approx, model_name='best_model')
    tuned_cm = tune_model(best_model)
    final_cm = finalize_model(tuned_cm)
    return final_cm

def classification_ml(path='sqlite:////data/main.db', batch_size=1000):
    conn = sql.connect(path)
    df1 = pd.read_sql_query(f"SELECT * FROM data LIMIT {batch_size}", conn)

    training= setup(data=df1, target='promoted',profile=True,log_profile=True)
    model=create_model("ada")

    model_ada=predict_model(model)
    profile_ada=ProfileReport(model_ada)
    profile_ada.to_file("templates/report.html")

    cm=create_model('ada')
    tuned_cm = tune_model(cm)
    final_cm = finalize_model(tuned_cm)
    return final_cm

def plot_acc(final_cm=classification_ml()):
    cm_acc=plot_model(final_cm, plot = 'auc', save=True)
def plot_pr(final_cm=classification_ml()):    
    cm_pr=plot_model(final_cm, plot = 'pr', save=True)
def plot_feature(final_cm=classification_ml()):    
    cm_feature=plot_model(final_cm, plot='feature', save=True)

