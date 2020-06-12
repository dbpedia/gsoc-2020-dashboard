import plotly.graph_objs as go


def ontologySunburst(plot_data):
    parents = [""]
    parents.extend(plot_data[0])
    labels = ["owlThing"]
    labels.extend(plot_data[1])

    ontologyFigure = go.Figure(
        go.Sunburst(labels=labels, parents=parents)
    )

    ontologyFigure.layout.update(
        width=1750,
        height=1750,
    )

    return ontologyFigure
