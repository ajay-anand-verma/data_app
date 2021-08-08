import os

from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd
import math

DATA_DIR = "basic/data"
STATE_POPULATION_DATA = os.path.join(DATA_DIR, "state_population.csv")

def layout(request):
    record_list = all_states()
    state_table_data = state_data('AP')
    context = {
        'table':record_list,
        'state_data':state_table_data
    }
    return render(request, 'basic/layout.html', context)

def state_data(state_code):
    if state_code == None:
        print("ERROR: State Code is MISSING!!!")
    data_file = os.path.join(DATA_DIR, 'states', state_code, 'population.csv')
    df = pd.read_csv(data_file)
    data_dict = df.to_dict()
    content = []
    for i in range(len(df)):
        rec = {}
        rec['ID'] = i + 1
        rec['District'] = data_dict['District'][i]
        rec['Area'] =   data_dict['Area'][i]
        rec['Population'] = data_dict['Population'][i]
        rec ['Density'] = data_dict['Density'][i]
        content.append(rec)
    return content

def get_state_data(request):
    record_list = all_states()
    state_table_data = state_data('AP')
    context = {
        'table':record_list,
        'state_data':state_table_data
    }
    return render(request, 'basic/show.html', context)


def all_states():
    df = pd.read_csv(STATE_POPULATION_DATA)
    data_dict = df.to_dict()
    content = []
    for i in range(len(df)):
        rec = {}
        rec['ID'] = i+1
        rec['State'] = data_dict['State'][i]
        rec['Districts'] = data_dict['Districts'][i]
        rec['Population'] = data_dict['Population'][i]
        rec['pov_rate'] = data_dict['Poverty Rate'][i]
        rec['pov_pop'] = math.ceil((data_dict['Population'][i]/100 ) * data_dict['Poverty Rate'][i])
        content.append(rec)
    return content

        

def home(request):
    record_list = all_states()
    context = {
        'table':record_list
        }
    return render(request, 'basic/layout.html', context)