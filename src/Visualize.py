import plotly.graph_objs as go


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
