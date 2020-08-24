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
