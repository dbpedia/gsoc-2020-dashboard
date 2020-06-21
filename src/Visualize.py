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
        polar_bgcolor='#212121',
        paper_bgcolor='#212121',
        font_size=15,
        font_color='#FFFFFF'
    )

    return ontologyFigure


def instanceCountPolar(plotData):
    barPolar = go.Figure(
        [go.Barpolar(r=plotData[1][:50], theta=plotData[0][:50], name='')]
    )
    return barPolar
