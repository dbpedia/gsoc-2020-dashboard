import plotly.graph_objs as go


def work_classes_pie(plot_data_subclasses, class_name):
    work_subclasses = plot_data_subclasses[plot_data_subclasses['class'] == class_name]
    subclasses_pie = go.Figure(go.Pie(
        labels=work_subclasses['subclass'],
        values=work_subclasses['tier2count'],
        textinfo='label+percent',
    ))

    subclasses_pie.update_layout(
        margin=dict(t=0, b=0, r=0, l=0, pad=0),
        plot_bgcolor='#292B2C',
        paper_bgcolor='#292B2C',
        font_size=15,
        font_color='#FFFFFF',
    )

    return subclasses_pie


def work_classes_bar(plot_data_subclasses, class_name):
    work_subclasses = plot_data_subclasses[plot_data_subclasses['class'] == class_name]
    subclasses_bar = go.Figure(go.Bar(
        y=work_subclasses['subclass'],
        x=work_subclasses['tier2count'],
        orientation='h'
    ))

    subclasses_bar.update_layout(
        margin=dict(t=0, b=0, r=0, l=0, pad=0),
        plot_bgcolor='#292B2C',
        paper_bgcolor='#292B2C',
        font_size=15,
        font_color='#FFFFFF',
    )

    return subclasses_bar


def triples():
    triples_figure = go.Figure(
        go.Scatter(x=['2020.0.1','2020.0.2','2020.0.3','2020.0.4'],
                   y=[51711866, 81711866, 281711866, 481711866],
                   mode='lines+markers', name='lines+markers')
    )

    triples_figure.update_layout(
        title='Growth of Triples Over Time',
        xaxis_title="Triples Count",
        yaxis_title="Versions",
        plot_bgcolor='#292B2C',
        paper_bgcolor='#292B2C',
        font_size=15,
        font_color='#FFFFFF',
        yaxis=dict(showgrid=False)
    )

    return triples_figure
