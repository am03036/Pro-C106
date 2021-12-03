import plotly.express as px
import csv
import numpy as np

def get_data_source(data_path):
    coffee = []
    sleep = []

    with open(data_path) as f:
        df = csv.DictReader(f)
        for row in df:
            coffee.append(float(row['Coffee in ml']))
            sleep.append(float(row['sleep in hours']))
    return {'x':coffee, 'y':sleep}

def find_corel(data_src):
    corelation = np.corrcoef(data_src['x'],data_src['y'])
    print("corelation between coffee consumed and sleep time is:",corelation[0,1])

def setup():
    data_path = 'data_coffee.csv'
    data_src = get_data_source(data_path)
    find_corel(data_src)

setup()

    