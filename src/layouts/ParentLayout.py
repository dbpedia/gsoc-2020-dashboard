import dash_core_components as dcc
import dash_html_components as html

documentation_link = 'https://github.com/dbpedia/gsoc-2020-dashboard/wiki'


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
                html.A(id='documentation', children=[html.Span('Documentation')], href='documentation_link', target='_blank',
                       className='navbar-text btn btn-outline-secondary about_content'),
                html.A(id='about', children=[html.Span('About')], href='/about',
                       className='navbar-text btn btn-outline-secondary about_content')
            ])
        ], className='navbar navbar-dark bg-dark', style={'padding-left': 20, 'padding-right': 20, 'padding-top': 3,
                                                          'padding-bottom': 3}),

        html.Div(id='container')

    ], className='w-100')
