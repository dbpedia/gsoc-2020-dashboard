import dash_core_components as dcc
import dash_html_components as html


def initializeHomePage():
    homePage = html.Div([

        html.Div([
            # html.Div([], className='col'),
            # html.Div([], className='col'),
            # html.Div([], className='col')
        ], className='row'),

        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        dcc.Textarea(id='sparql-query-input', placeholder='SPARQL Query Editor',
                                     style={'width': '100%', 'align-content': 'center'})
                    ], className='col', style={'margin': 20}),
                ], className='row w100'),

                html.Div([
                    html.Div([
                        dcc.Dropdown(id='format-dropdown',
                                     options=[
                                         {'label': 'CSV', 'value': 'CSV'},
                                         {'label': 'TSV', 'value': 'TSV'},
                                         {'label': 'JSON', 'value': 'JSON'},
                                         {'label': 'HTML', 'value': 'HTML'}
                                     ],
                                     value='CSV')
                    ], className='col'),
                    html.Div([
                        dcc.Dropdown(id='core-version-dropdown',
                                     options=[
                                         {'label': '2020.0.1', 'value': '2020.0.1'},
                                         {'label': '2020.1.1', 'value': '2020.1.1'}
                                     ],
                                     value='2020.1.1')
                    ], className='col'),
                    html.Div([
                        dcc.Input(id='execution-timeout-input',
                                  type='numeric',
                                  placeholder='Value greater than 1000',
                                  style={'width': '100%', 'height': '100%', 'border-radius': '5px',
                                         'border': '1px solid #C0C0C0', 'padding-left': 10, 'padding-right': 10})
                    ], className='col'),
                    html.Div([
                        html.Button('Run Query', id='run-query-button', className='btn',
                                    style={'width': '100%', 'height': '100%', 'background-color': '#e8aa24',
                                           'color': '#FFFFFF'})
                    ], className='col'),
                    html.Div([
                        html.Button('Download', id='download-button', className='btn',
                                    style={'width': '100%', 'height': '100%', 'background-color': '#e8aa24',
                                           'color': '#FFFFFF'})
                    ], className='col'),
                ], className='row w-100 m-0 p-0')
            ], className='card-body')
        ], className='card', style={'background-color': '#08415f', 'margin': 20}),

    ])

    return homePage
