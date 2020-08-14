from io import StringIO
from os import path

import pandas as pd
import plotly.graph_objs as go
from SPARQLWrapper import JSON, CSV

import src.CSVParser as CSVP
import src.Constants as Constants
import src.JSONParser as JP
import src.RequestData as RD

dataPath = 'data/v1'
bgColor = '#292B2C'
fontColor = '#FFFFFF'
fontSize = 15
height = 500
spacing = dict(t=0, b=0, r=0, l=0, pad=0)


def ontologySunburst(ontologyData):
    ontologySunburstFigure = go.Figure(go.Sunburst(labels=ontologyData['labels'], parents=ontologyData['parents'], maxdepth=2))
    ontologyTreemapFigure = go.Figure(go.Treemap(labels=ontologyData['labels'], parents=ontologyData['parents']))

    ontologySunburstFigure.update_layout(margin=spacing, height=height, polar_bgcolor=bgColor, paper_bgcolor=bgColor,
                                         font_size=fontSize, font_color=fontColor)
    ontologyTreemapFigure.update_layout(margin=spacing, height=height, polar_bgcolor=bgColor, paper_bgcolor=bgColor,
                                        font_size=fontSize, font_color=fontColor)

    return [ontologyTreemapFigure, ontologySunburstFigure]


def ontologyHierarchy():
    ontologyData = ''
    if path.exists(dataPath + '/Ontologies.csv'):
        ontologyData = pd.read_csv(dataPath + '/Ontologies.csv')
        print('ontologies fetched from the file')
    else:
        results = RD.sparqlWrapper(Constants.ONTOLOGY_HIERARCHY, JSON)
        ontologyData = JP.toOntologyHierarchy(results)
        ontologyData.to_csv('data/v1/Ontologies.csv', index=False, index_label=False)
        print('ontologies fetched using query')
    return ontologySunburst(ontologyData)


def parentClassesBar(plotDataParent):
    barColors = ['#004D40', '#BF360C', '#01579B', '#FFAB00', '#FFFFFF']

    instancesFigure = go.Figure(go.Bar(x=plotDataParent['tier2count'], y=plotDataParent['class'], orientation='h',
                                       marker=dict(color=barColors)))

    instancesFigure.update_layout(height=height, margin=spacing, plot_bgcolor=bgColor, paper_bgcolor=bgColor, font_size=fontSize,
                                  font_color=fontColor, yaxis=dict(showgrid=False))

    return instancesFigure


def instanceCountBar(plotDataParent):
    instanceCountsFigures = dict()
    instanceCountsFigures['parent'] = parentClassesBar(plotDataParent)
    return instanceCountsFigures


def instanceCount():
    parentClasses, instancesCount = '', ''
    if path.exists(dataPath + '/InstancesCount.csv') and path.exists(dataPath + '/ParentClasses.csv'):
        parentClasses = pd.read_csv(dataPath + '/ParentClasses.csv')
        instancesCount = pd.read_csv(dataPath + '/InstancesCount.csv')
        print('instances fetched from the file')
    else:
        results = RD.sparqlWrapper(Constants.INSTANCES_COUNT, CSV)
        parentClasses, instancesCount = CSVP.toInstanceCount(results)
        parentClasses.to_csv('data/v1/ParentClasses.csv', index_label=False, index=False)
        instancesCount.to_csv('data/v1/InstancesCount.csv', index_label=False, index=False)
    return instanceCountBar(parentClasses)


def generalStatistics():
    generalStatistics = dict()

    for targetStat, query in Constants.GENERAL_STATISTICS.items():
        stats = RD.sparqlWrapper(query, CSV)
        stats = pd.read_csv(StringIO(stats.decode("utf-8")), sep=',').iloc[0]['counts']
        generalStatistics[targetStat] = stats
    print(generalStatistics)
    return generalStatistics


def userQuery(query):
    results = RD.sparqlWrapper(query, CSV)
    table = CSVP.parseQueryResponse(results)
    return table
