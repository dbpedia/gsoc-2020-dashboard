import json
from io import StringIO
from os import path

import pandas as pd
import plotly.graph_objs as go
from SPARQLWrapper import JSON, CSV

import src.CSVParser as CSVP
import src.Constants as Constants
import src.JSONParser as JP
import src.RequestData as RD

data_path = 'data/v1'
bg_color = '#292B2C'
font_color = '#FFFFFF'
font_size = 15
height = 500
spacing = dict(t=0, b=0, r=0, l=0, pad=0)


def ontology_figures(ontology_data):
    ontology_sunburst_figure = go.Figure(go.Sunburst(labels=ontology_data['labels'], parents=ontology_data['parents'], maxdepth=2))
    ontology_treemap_figure = go.Figure(go.Treemap(labels=ontology_data['labels'], parents=ontology_data['parents']))

    ontology_sunburst_figure.update_layout(margin=spacing, height=height, polar_bgcolor=bg_color, paper_bgcolor=bg_color,
                                           font_size=font_size, font_color=font_color)
    ontology_treemap_figure.update_layout(margin=spacing, height=height, polar_bgcolor=bg_color, paper_bgcolor=bg_color,
                                          font_size=font_size, font_color=font_color)

    return [ontology_treemap_figure, ontology_sunburst_figure]


def ontology_hierarchy():
    ontology_data = ''
    if path.exists(data_path + '/Ontologies.csv'):
        ontology_data = pd.read_csv(data_path + '/Ontologies.csv')
        print('ontologies fetched from the file')
    else:
        results = RD.sparql_wrapper(Constants.ONTOLOGY_HIERARCHY, JSON)
        ontology_data = JP.to_ontology_hierarchy(results)
        ontology_data.to_csv('data/v1/Ontologies.csv', index=False, index_label=False)
        print('ontologies fetched using query')
    return ontology_data, ontology_figures(ontology_data)


def all_instances_count_plot(all_instances_data):
    all_instances_figure = go.Figure(go.Bar(x=all_instances_data['instancecount'], y=all_instances_data['class'],
                                            orientation='h'))

    all_instances_figure.update_layout(height=height, margin=spacing, plot_bgcolor=bg_color, paper_bgcolor=bg_color, font_size=font_size,
                                       font_color=font_color, yaxis=dict(showgrid=False))

    return all_instances_figure


def all_instances_count():
    all_instances_data = ''
    if path.exists(data_path + '/AllInstances.csv'):
        all_instances_data = pd.read_csv(data_path + '/AllInstances.csv')
        print('all instances count fetched from the file')
    else:
        results = RD.sparql_wrapper(Constants.ALL_INSTANCES_COUNT, CSV)
        all_instances_data = CSVP.to_all_instances_count(results)
        all_instances_data.to_csv('data/v1/AllInstances.csv', index=False, index_label=False)
        print('all instances fetched using query')
    return all_instances_data, all_instances_count_plot(all_instances_data)


def get_general_statistics():
    general_statistics = dict()

    if path.exists(data_path + '/GeneralStatistics.json'):
        with open(data_path + '/GeneralStatistics.json') as general_statistics_json:
            general_statistics = json.load(general_statistics_json)
            print('general statistics fetched from the file')
    else:
        for targetStat, query in Constants.GENERAL_STATISTICS.items():
            stats = RD.sparql_wrapper(query, CSV)
            stats = pd.read_csv(StringIO(stats.decode("utf-8")), sep=',').iloc[0]['counts']
            general_statistics[targetStat] = str(stats)
        with open(data_path + '/GeneralStatistics.json', 'w') as general_statistics_json:
            json.dump(general_statistics, general_statistics_json)
        print('general statistics fetched using query')
    return general_statistics


def user_query(query):
    results = RD.sparql_wrapper(query, CSV)
    table = CSVP.parse_query_response(results)
    return table
