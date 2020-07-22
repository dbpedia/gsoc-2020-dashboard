import dash_core_components as dcc
import dash_html_components as html


def homePageLayout(dashApp):
    dashApp.layout = html.Div([

        dcc.Location(id='route', refresh=False),

        # navigation bar
        html.Nav(children=[
            html.A(children=[
                html.Img(src='https://wiki.dbpedia.org/sites/default/files/DBpediaLogoFull.png', height=40,
                         className='d-inline-block')
            ], className='navbar-brand')
        ], className='navbar navbar-dark bg-dark'),

        # tabs
        html.Div([
            html.Div(id='clicked-button', children='ontologies:0 instancescount:0 last:nan', style={'display': 'none'}),
            html.Div([
                html.Button('Ontologies', id='btn_ontologies', n_clicks=0,
                            className='btn btn-secondary btn-lg btn-block')
            ], className='col m-0 p-0'),
            html.Div([
                html.Button('Instances Count', id='btn_instancescount', n_clicks=0,
                            className='btn btn-secondary btn-lg btn-block')
            ], className='col m-0 p-0')
        ], className='row w-100 m-0 p-0'),
        html.Div(id='display-clicked', children=''),

        # tidy tree
        # html.Div([
        #     dcc.Loading(id='tidy_tree_loader', type='cube', className='h-100 align-items-center', children=[
        #         html.Iframe(src='../assets/radial.html', style={'background': '#FFFFFF', 'width': 1500, 'height':1500}),
        #     ])
        # ], className='card w-100 bg-dark'),

        # container for ontologies and instances count
        html.Div(id='container'),

    ], className='w-100')
