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
        font_size=15,
        font_color='#000000',
    )

    return subclasses_pie


def work_classes_bar(plot_data_subclasses, class_name):
    work_subclasses = plot_data_subclasses[plot_data_subclasses['class'] == class_name]
    work_subclasses = work_subclasses[work_subclasses['tier2count'] != 0]
    subclasses_bar = go.Figure(go.Bar(
        y=work_subclasses['subclass'],
        x=work_subclasses['tier2count'],
        orientation='h'
    ))

    subclasses_bar.update_layout(
        margin=dict(t=0, b=0, r=0, l=0, pad=0),
        font_size=15,
        font_color='#000000',
    )

    return subclasses_bar


def triples(triples_count):
    print(triples_count)
    triples_figure = go.Figure(
        go.Scatter(x=triples_count['version'],
                   y=triples_count['triplescount'],
                   mode='lines+markers', name='lines+markers')
    )

    triples_figure.update_layout(
        margin=dict(t=30, b=0, r=0, l=0, pad=0),
        title='Growth of Triples Over Time',
        title_x=0.5,
        plot_bgcolor='#263238',
        paper_bgcolor='#263238',
        xaxis_title="Versions",
        yaxis_title="Triples Count",
        font_size=15,
        font_color='#FFFFFF',
        yaxis=dict(showgrid=False)
    )

    return triples_figure
