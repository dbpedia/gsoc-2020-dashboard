import dash_core_components as dcc
import dash_html_components as html


def initializeInstancesCount(instancesCountFigures):
    instancesCount = html.Div(id='instances_count_container', children=[

        html.Div([
            dcc.Loading(id='parent_instances_loader', type='cube',
                        className='h-100 align-items-center',
                        children=[
                            html.Div(id='parent_instances', children=[
                                dcc.Graph(id='parent_instances_bar', figure=instancesCountFigures['parent'])
                            ])
                        ])
        ]),

        html.Div([
            html.Label('', id='parentclass_label', className='text-center w-100 text-white'),
        ], className='m-3'),

        html.Div([
            html.Div([
                dcc.Loading(id='subclasses_plot_loader', type='cube',
                            className='h-100 align-items-center',
                            children=[
                                html.Div(id='subclasses_instances')
                            ])
            ], className='col'),
        ], className='row w-100')

    ], className='w-100')

    return instancesCount
