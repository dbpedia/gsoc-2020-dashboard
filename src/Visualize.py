import numpy as np
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


def instanceCountPolar(plotData):
    data = plotData['Work']
    x = np.log10(list(data.values()))
    print(data.values(), x)
    barPolar = go.Figure(
        go.Barpolar(r=x, theta=list(data.keys())[1:], text=list(data.values()))
    )

    barPolar.update_layout(polar_bgcolor='#292B2C', paper_bgcolor='#292B2C', polar=dict(radialaxis=dict(visible=False)),
                           font_color='#FFFFFF')
    return barPolar
