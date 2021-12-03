import plotly.express as px
import csv
import numpy as np

def get_data_source(data_path):
    marks = []
    days = []

    with open(data_path) as f:
        df = csv.DictReader(f)
        for row in df:
            marks.append(float(row['Marks In Percentage']))
            days.append(float(row['Days Present']))
    return {'x':marks, 'y':days}

def find_corel(data_src):
    corelation = np.corrcoef(data_src['x'],data_src['y'])
    print("corelation between marks scored and days present is:",corelation[0,1])

def setup():
    data_path = 'data_days.csv'
    data_src = get_data_source(data_path)
    find_corel(data_src)

setup()

    