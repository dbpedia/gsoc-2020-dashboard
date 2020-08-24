import dash_core_components as dcc
import dash_html_components as html


def root_layout(dashApp):
    dashApp.layout = html.Div([

        dcc.Location(id='route', refresh=False),

        # navigation bar
        html.Nav(children=[
            html.A(href='/', children=[
                html.Img(src='https://wiki.dbpedia.org/sites/default/files/DBpediaLogoFull.png', height=45,
                         className='d-inline-block')
            ], className='navbar-brand'),
            html.Div([
                html.A(id='documentation', children=[html.Span('Documentation')], href='/documentation',
                       className='navbar-text btn btn-outline-secondary about_content'),
                html.A(id='about', children=[html.Span('About')], href='/about',
                       className='navbar-text btn btn-outline-secondary about_content')
            ])
        ], className='navbar navbar-dark bg-dark', style={'padding-left': 20, 'padding-right': 20, 'padding-top': 3,
                                                          'padding-bottom': 3}),

        html.Div(id='container')

        # tidy tree
        # html.Div([
        #     dcc.Loading(id='tidy_tree_loader', type='cube', className='h-100 align-items-center', children=[
        #         html.Iframe(src='../assets/radial.html', style={'background': '#FFFFFF', 'width': 1500, 'height':1500}),
        #     ])
        # ], className='card w-100 bg-dark'),

        # container for ontologies and instances count

    ], className='w-100')
