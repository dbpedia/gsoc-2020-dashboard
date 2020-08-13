import plotly.graph_objs as go
import pandas as pd

def ontologySunburst(plotData):

    ontologySunburstFigure = go.Figure(
        go.Sunburst(labels=plotData['labels'], parents=plotData['parents'], maxdepth=2)
    )

    ontologySunburstFigure.update_layout(
        margin=dict(t=0, b=0, r=0, l=0, pad=0),
        height=500,
        polar_bgcolor='#292B2C',
        paper_bgcolor='#292B2C',
        font_size=15,
        font_color='#FFFFFF'
    )

    ontologyTreemapFigure = go.Figure(
        go.Treemap(labels=plotData['labels'], parents=plotData['parents'])
    )

    ontologyTreemapFigure.update_layout(
        margin=dict(t=0, b=0, r=0, l=0, pad=0),
        height=500,
        polar_bgcolor='#292B2C',
        paper_bgcolor='#292B2C',
        font_size=15,
        font_color='#FFFFFF'
    )

    return [ontologyTreemapFigure, ontologySunburstFigure]


def parentClassesBar(plotDataParent):
    barColors = ['#004D40', '#BF360C', '#01579B', '#FFAB00', '#FFFFFF']

    instancesFigure = go.Figure(go.Bar(
        x=plotDataParent['tier2count'],
        y=plotDataParent['class'],
        orientation='h',
        marker=dict(color=barColors)
    ))

    instancesFigure.update_layout(
        height=500,
        margin=dict(t=0, b=0, r=0, l=0, pad=0),
        plot_bgcolor='#292B2C',
        paper_bgcolor='#292B2C',
        font_size=15,
        font_color='#FFFFFF',
        yaxis=dict(showgrid=False)
    )

    # plt.plot(instancesFigure, filename='test.html'
    return instancesFigure


def workClassesPie(plotDataSubClasses, className):
    workSubClasses = plotDataSubClasses[plotDataSubClasses['class'] == className]
    subclassesPie = go.Figure(go.Pie(
        labels=workSubClasses['subclass'],
        values=workSubClasses['tier2count'],
        textinfo='label+percent',
    ))

    subclassesPie.update_layout(
        margin=dict(t=0, b=0, r=0, l=0, pad=0),
        plot_bgcolor='#292B2C',
        paper_bgcolor='#292B2C',
        font_size=15,
        font_color='#FFFFFF',
    )

    return subclassesPie


def workClassesBar(plotDataSubClasses, className):
    workSubClasses = plotDataSubClasses[plotDataSubClasses['class'] == className]
    subclassesBar = go.Figure(go.Bar(
        y=workSubClasses['subclass'],
        x=workSubClasses['tier2count'],
        orientation='h'
    ))

    subclassesBar.update_layout(
        margin=dict(t=0, b=0, r=0, l=0, pad=0),
        plot_bgcolor='#292B2C',
        paper_bgcolor='#292B2C',
        font_size=15,
        font_color='#FFFFFF',
    )

    return subclassesBar


def instanceCountBar(plotDataParent, plotDataSubClasses):
    instanceCountsFigures = dict()

    instanceCountsFigures['parent'] = parentClassesBar(plotDataParent)
    instanceCountsFigures['Work+Pie'] = workClassesPie(plotDataSubClasses, 'Work')
    instanceCountsFigures['Place+Pie'] = workClassesPie(plotDataSubClasses, 'Place')
    instanceCountsFigures['Person+Pie'] = workClassesPie(plotDataSubClasses, 'Person')
    instanceCountsFigures['Organisation+Pie'] = workClassesPie(plotDataSubClasses, 'Organisation')
    instanceCountsFigures['Event+Pie'] = workClassesPie(plotDataSubClasses, 'Event')

    # instanceCountsFigures['Work+Bar'] = workClassesBar(plotDataSubClasses, 'Work')
    # instanceCountsFigures['Place+Bar'] = workClassesBar(plotDataSubClasses, 'Place')
    # instanceCountsFigures['Person+Bar'] = workClassesBar(plotDataSubClasses, 'Person')
    # instanceCountsFigures['Organisation+Bar'] = workClassesBar(plotDataSubClasses, 'Organisation')
    # instanceCountsFigures['Event+Bar'] = workClassesBar(plotDataSubClasses, 'Event')

    # instanceCountsFigures['Work']['Line'] = workClassesLine(plotDataSubClasses)

    return instanceCountsFigures
