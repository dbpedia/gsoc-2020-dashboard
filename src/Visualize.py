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


def instanceCountPolar(plotData, classNames):
    barPolars = []
    colors = {
        'Event': '#004D40',
        'Person': '#BF360C',
        'Organisation': '#01579B',
        'Work': '#FFAB00',
        'Place': '#FFFFFF'
    }

    thetas = []
    mixedValues = []
    mixedColors = []

    for className in classNames:
        data = plotData[className]
        print(data.values())
        x = np.log10(list(data.values()))
        thetas.extend(list(data.keys()))
        mixedValues.extend(x)
        mixedColors.extend([colors[className]] * len(x))

    print(thetas)
    print(mixedValues)
    print(mixedColors)

    barPolar = go.Figure(
        go.Barpolar(r=mixedValues, theta=thetas, text=mixedValues,
                    marker=dict(color=mixedColors))
    )

    barPolar.update_layout(polar_bgcolor='#292B2C', paper_bgcolor='#292B2C',
                           font_color='#FFFFFF', title='Instances Count', height=1000)

    barPolars.append(barPolar)

    return barPolar
