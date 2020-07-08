import plotly.graph_objs as go


def ontologySunburst(plotData):
    parents = [""]
    parents.extend(plotData[0])
    labels = ["owlThing"]
    labels.extend(plotData[1])

    ontologyFigure = go.Figure(
        go.Sunburst(labels=labels, parents=parents)
    )

    ontologyFigure.update_layout(
        margin=dict(t=0, b=0, r=0, l=0, pad=0),
        height=1300,
        polar_bgcolor='#292B2C',
        paper_bgcolor='#292B2C',
        font_size=15,
        font_color='#FFFFFF'
    )

    return ontologyFigure


def parentClassesBar(plotDataParent):
    barColors = ['#004D40', '#BF360C', '#01579B', '#FFAB00', '#FFFFFF']

    instancesFigure = go.Figure(go.Bar(
        x=plotDataParent['tier2count'],
        y=plotDataParent['class'],
        orientation='h',
        marker=dict(color=barColors)
    ))

    instancesFigure.update_layout(
        height=300,
        margin=dict(t=0, b=0, r=0, l=0, pad=0),
        plot_bgcolor='#292B2C',
        paper_bgcolor='#292B2C',
        font_size=15,
        font_color='#FFFFFF',
        yaxis=dict(showgrid=False)
    )

    return instancesFigure


def workClassesPie(plotDataSubClasses):
    workSubClasses = plotDataSubClasses[plotDataSubClasses['class'] == 'Work']
    subclassesPie = go.Figure(go.Pie(
        labels=workSubClasses['subclass'],
        values=workSubClasses['tier2count'],
        textinfo='label+percent',
        insidetextorientation='radial'
    ))

    return subclassesPie


def workClassesPolar(plotDataSubClasses):
    workSubClasses = plotDataSubClasses[plotDataSubClasses['class'] == 'Work']
    subclassesPie = go.Figure(go.Pie(
        labels=workSubClasses['subclass'],
        values=workSubClasses['tier2count'],
        textinfo='label+percent',
        insidetextorientation='radial'
    ))

    return subclassesPie


def instanceCountBar(plotDataParent, plotDataSubClasses):
    instanceCountsFigures = dict()

    instanceCountsFigures['parent'] = parentClassesBar(plotDataParent)
    instanceCountsFigures['Work+Pie'] = workClassesPie(plotDataSubClasses)
    instanceCountsFigures['Work+Polar'] = workClassesPolar(plotDataSubClasses)
    # instanceCountsFigures['Work']['Line'] = workClassesLine(plotDataSubClasses)

    return instanceCountsFigures

