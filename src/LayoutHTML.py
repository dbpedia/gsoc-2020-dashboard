import dash_core_components as dcc
import dash_html_components as html


def homePageLayout(dashApp):
    dashApp.layout = html.Div([

        dcc.Location(id='url', refresh=False),

        # tabs
        dcc.Tabs(id='class_details', value='ontology', children=[
            dcc.Tab(label='Ontology Sunburst', value='ontology'),
            dcc.Tab(label='Instances Count', value='instance_count')
        ], colors={
            "border": "#212121",
            "primary": "#212121",
            "background": "#9E9E9E"
        }),

        # tidy tree
        # html.Div([
        #     dcc.Loading(id='tidy_tree_loader', type='cube', className='h-100 align-items-center', children=[
        #         html.Iframe(src='../assets/radial.html', style={'background': '#FFFFFF', 'width': 1500, 'height':1500}),
        #     ])
        # ], className='card w-100 bg-dark'),

        # plot ontology hierarchy graphs
        html.Div(id='ontology_container', children=[
            dcc.Loading(id='ontology_loader', type='cube', className='h-100 align-items-center', children=[
                html.Div(id='ontology')
            ])
        ], className='card w-100 bg-dark'),

        # plot parent and subclasses instance count graphs
        html.Div(id='instances_count_container', children=[

            html.Div([
                dcc.Loading(id='instances_event_loader', type='cube',
                            className='h-100 align-items-center',
                            children=[
                                html.Div(id='parent_instances')
                            ])
            ]),

        ], className='w-100 bg-dark', style={'display': 'none'})

    ], className='w-100')
