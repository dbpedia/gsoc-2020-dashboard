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


def ontology_sunburst(ontology_data):
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
    return ontology_sunburst(ontology_data)


def parent_classes_bar(plot_data_parent):
    bar_colors = ['#004D40', '#BF360C', '#01579B', '#FFAB00', '#FFFFFF']

    instances_figure = go.Figure(go.Bar(x=plot_data_parent['tier2count'], y=plot_data_parent['class'], orientation='h',
                                        marker=dict(color=bar_colors)))

    instances_figure.update_layout(height=height, margin=spacing, plot_bgcolor=bg_color, paper_bgcolor=bg_color, font_size=font_size,
                                   font_color=font_color, yaxis=dict(showgrid=False))

    return instances_figure


def instance_count_bar(plot_data_parent):
    instance_counts_figures = dict()
    instance_counts_figures['parent'] = parent_classes_bar(plot_data_parent)
    return instance_counts_figures


def instance_count():
    parent_classes, instances_count = '', ''

    if path.exists(data_path + '/InstancesCount.csv') and path.exists(data_path + '/ParentClasses.csv'):
        parent_classes = pd.read_csv(data_path + '/ParentClasses.csv')
        instances_count = pd.read_csv(data_path + '/InstancesCount.csv')
        print('instances count fetched from the file')
    else:
        results = RD.sparql_wrapper(Constants.INSTANCES_COUNT, CSV)
        parent_classes, instances_count = CSVP.to_instance_count(results)
        parent_classes.to_csv('data/v1/ParentClasses.csv', index_label=False, index=False)
        instances_count.to_csv('data/v1/InstancesCount.csv', index_label=False, index=False)
        print('instances count fetched using query')
    return instance_count_bar(parent_classes)


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
