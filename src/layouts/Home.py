import dash_core_components as dcc
import dash_html_components as html

import src.Visualize as VI


def initialize_home_page(general_statistics, ontology_figures, triples_count):
    home_page = html.Div([

        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.Span('Dashboard Status ', id='dashboard-status-label', className='m-0 p-0'),
                        html.Span('Connected', id='dashboard-status', className='m-0 badge badge-pill badge-success')
                    ], className='col'),
                ], className='row w100'),
            ], className='card-body')
        ], className='card p-0', style={'background-color': '#E0E0E0', 'margin': 20, 'border-radius': '5px',
                                        'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.20), 0 6px 20px 0 rgba(0, 0, 0, 0.20)'}),

        # SPORTAL Statistics 1
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.Label('Total Triples', style={'color': '#000000', 'margin': 0, 'padding': 0}),
                        dcc.Loading(type='dot', children=[
                            html.Label(id='total-triples-label',
                                       children=general_statistics['TOTAL_TRIPLES'],
                                       style={'font-size': '30px', 'color': '#000000', 'margin': 0,
                                              'line-height': '120%'})
                        ])
                    ], className='card-body', style={'padding': 15})
                ], className='card text-center', style={'background-color': '#EEEEEE', 'border-radius': '5px',
                                                        'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.20),'
                                                                      '0 6px 20px 0 rgba(0, 0, 0, 0.20)'})
            ], className='col'),
            html.Div([
                html.Div([
                    html.Div([
                        html.Label('Total Classes', style={'color': '#000000', 'margin': 0, 'padding': 0}),
                        dcc.Loading(type='dot', children=[
                            html.Label(id='total-classes-label',
                                       children=general_statistics['TOTAL_CLASSES'],
                                       style={'font-size': '30px', 'color': '#000000', 'margin': 0,
                                              'line-height': '120%'})
                        ])
                    ], className='card-body', style={'padding': 15})
                ], className='card text-center', style={'background-color': '#EEEEEE', 'border-radius': '5px',
                                                        'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.20),'
                                                                      '0 6px 20px 0 rgba(0, 0, 0, 0.20)'})
            ], className='col'),
            html.Div([
                html.Div([
                    html.Div([
                        html.Label('Total Properties', style={'color': '#000000', 'margin': 0, 'padding': 0}),
                        dcc.Loading(type='dot', children=[
                            html.Label(id='total-properties-label',
                                       children=general_statistics['TOTAL_PROPERTIES'],
                                       style={'font-size': '30px', 'color': '#000000', 'margin': 0,
                                              'line-height': '120%'})
                        ])
                    ], className='card-body', style={'padding': 15})
                ], className='card text-center', style={'background-color': '#EEEEEE', 'border-radius': '5px',
                                                        'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.20),'
                                                                      '0 6px 20px 0 rgba(0, 0, 0, 0.20)'})
            ], className='col')
        ], className='row', style={'margin': 20}),

        # plots
        html.Div([
            html.Div([
                html.Div(children=[
                    html.Div([
                        html.Div([
                            html.P('Click on class names to expand hierarchy and get instances count on bar graph',
                                   className='mt-2 mb-0'),
                            html.P('Click Ontologies button to change hierarchy plot',
                                   className='mt-0 mb-2')
                        ], className='col text-center'),
                    ], className='row w-100 m-0 p-0'),

                    html.Div(children=[

                        # ontologies
                        html.Div(children=[
                            html.Div(children=[
                                html.Button('Ontologies', id='btn_ontologies', n_clicks=0,
                                            className='btn btn-lg btn-block',
                                            style={'background-color': '#EEEEEE'})
                            ], className='col m-0 p-0'),
                            html.Div([
                                dcc.Loading(type='cube',
                                            className='h-100 align-items-center',
                                            children=[
                                                html.Div(id='ontology_container', children=[
                                                    dcc.Graph(id='ontology', figure=ontology_figures[1])
                                                ])
                                            ])
                            ])
                        ], className='col p-0', style={'min-width': '500px'}),

                        # instances count
                        html.Div(children=[
                            html.Div([
                                html.Button('Instances Count', id='btn_instancescount', n_clicks=0,
                                            className='btn btn-lg btn-block', disabled=True,
                                            style={'background-color': '#EEEEEE'})
                            ], className='col m-0 p-0'),
                            html.Div([
                                dcc.Loading(type='cube',
                                            className='h-100 align-items-center',
                                            children=[
                                                html.Div(id='parent_instances')
                                            ])
                            ]),
                        ], className='col p-0', style={'min-width': '500px'}),

                    ], className='row w-100 m-0 p-4',
                        style={'background-color': '#263238', 'border-radius': '5px',
                               'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.20), 0 6px 20px 0 rgba(0, 0, 0, 0.20)'})
                ]),
            ], className='card-body p-0')
        ], className='card', style={'margin': 30}),

        # SPORTAL Statistics 2
        html.Div([

            # subjects
            # html.Div([
            #     html.Div([
            #         html.Div([
            #             html.Label('Distinct Subject Nodes', style={'color': '#FFFFFF', 'margin': 0, 'padding': 0}),
            #             dcc.Loading(type='dot', children=[
            #                 html.Label(id='distinct-subjects-label',
            #                            children=[distinctSubjects],
            #                            style={'font-size': '30px', 'color': '#FFFFFF', 'margin': 0,
            #                                   'line-height': '120%'})
            #             ])
            #         ], className='card-body', style={'padding': 15})
            #     ], className='card text-center', style={'background-color': '#263238', 'border-radius': '5px',
            #                                             'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.48),'
            #                                                           '0 6px 20px 0 rgba(0, 0, 0, 0.48)'})
            # ], className='col'),
            html.Div([
                html.Div([
                    html.Div([
                        html.Label('Blank Subject Nodes', style={'color': '#000000', 'margin': 0, 'padding': 0}),
                        dcc.Loading(type='dot', children=[
                            html.Label(id='blank-subjects-label',
                                       children=general_statistics['BLANK_SUBJECTS'],
                                       style={'font-size': '30px', 'color': '#000000', 'margin': 0,
                                              'line-height': '120%'})
                        ])
                    ], className='card-body', style={'padding': 15})
                ], className='card text-center', style={'background-color': '#EEEEEE', 'border-radius': '5px',
                                                        'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.20),'
                                                                      '0 6px 20px 0 rgba(0, 0, 0, 0.20)'})
            ], className='col'),

            # objects
            # html.Div([
            #     html.Div([
            #         html.Div([
            #             html.Label('Distinct Object Nodes', style={'color': '#FFFFFF', 'margin': 0, 'padding': 0}),
            #             dcc.Loading(type='dot', children=[
            #                 html.Label(id='distinct-objects-label',
            #                            children=[distinctObjects],
            #                            style={'font-size': '30px', 'color': '#FFFFFF', 'margin': 0,
            #                                   'line-height': '120%'})
            #             ])
            #         ], className='card-body', style={'padding': 15})
            #     ], className='card text-center', style={'background-color': '#263238', 'border-radius': '5px',
            #                                             'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.48),'
            #                                                           '0 6px 20px 0 rgba(0, 0, 0, 0.48)'})
            # ], className='col'),
            html.Div([
                html.Div([
                    html.Div([
                        html.Label('Blank Object Nodes', style={'color': '#000000', 'margin': 0, 'padding': 0}),
                        dcc.Loading(type='dot', children=[
                            html.Label(id='blank-objects-label',
                                       children=general_statistics['BLANK_OBJECTS'],
                                       style={'font-size': '30px', 'color': '#000000', 'margin': 0,
                                              'line-height': '120%'})
                        ])
                    ], className='card-body', style={'padding': 15})
                ], className='card text-center', style={'background-color': '#EEEEEE', 'border-radius': '5px',
                                                        'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.20),'
                                                                      '0 6px 20px 0 rgba(0, 0, 0, 0.20)'})
            ], className='col'),
        ], className='row', style={'margin': 20}),

        html.Div([
            html.Div([
                dcc.Graph(id='triples', figure=VI.triples(triples_count))
            ], className='card-body p-0')
        ], className='card p-3', style={'margin': 30, 'background-color': '#263238', 'border-radius': '5px',
                                        'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.20),'
                                                      '0 6px 20px 0 rgba(0, 0, 0, 0.20)'}),

        # SPARQL Editor
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        dcc.Input(id='sparql-query-input', placeholder='SPARQL Query Editor', debounce=True,
                                  style={'width': '100%', 'align-content': 'center', 'padding': 10,
                                         'border-radius': '5px', 'border': '1px solid #C0C0C0'})
                    ], className='col', style={'margin': 20}),
                ], className='row w100'),

                html.Div([
                    html.Div([
                        dcc.Dropdown(id='format-dropdown',
                                     options=[
                                         {'label': 'CSV', 'value': 'CSV'},
                                     ],
                                     value='CSV')
                    ], className='col'),
                    html.Div([
                        dcc.Dropdown(id='core-version-dropdown',
                                     options=[
                                         {'label': '2020.0.1', 'value': '2020.0.1'},
                                     ],
                                     value='2020.0.1')
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
                                    style={'width': '100%', 'height': '100%', 'background-color': '#37474F',
                                           'color': '#FFFFFF'})
                    ], className='col'),
                    html.Div([
                        html.Button('Download', id='download-button', className='btn', disabled=True,
                                    style={'width': '100%', 'height': '100%', 'background-color': '#37474F',
                                           'color': '#FFFFFF'})
                    ], className='col'),
                ], className='row w-100 m-0 p-0'),

                html.Div([
                    html.Div(id='response-datatable-div', className='col', style={'margin': 20})
                ], className='row w-100 m-0 p-0')
            ], className='card-body')
        ], className='card', style={'background-color': '#E0E0E0', 'margin': 20, 'border-radius': '10px',
                                    'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.20), 0 6px 20px 0 rgba(0, 0, 0, 0.20)'}),

    ])

    return home_page
