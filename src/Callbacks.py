import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import requests
from dash.dependencies import Output, Input

import src.LayoutFigures as LF
from src.layouts.About import initialize_about_page
from src.layouts.Home import initialize_home_page


def initialize_callbacks(dashApp):
    ontology_data, ontology_figures = LF.ontology_hierarchy()
    all_instances_count_data, all_instances_count_figure = LF.all_instances_count()
    general_statistics = LF.get_general_statistics()
    triples_count = pd.read_csv('data/v1/TriplesCount.csv')

    @dashApp.callback(
        [Output('dashboard-status', 'children'),
         Output('dashboard-status', 'className')],
        [Input('dashboard-status-interval', 'n_intervals')]
    )
    def update_status(n_intervals):
        response = requests.post('http://127.0.0.1:5000/connectionstatus',
                                 json={
                                     'dbpediadashboard_image': 'karankharecha/dbpediadashboard:latest',
                                     'dbpediadashboard_container': 'dbdash'
                                 })
        response = response.json()
        if response['status'] == 'connected':
            return response['status'], 'm-0 badge badge-pill badge-success'
        elif response['status'] == 'disconnected':
            return response['status'], 'm-0 badge badge-pill badge-warning'
        else:
            return response['status'], 'm-0 badge badge-pill badge-danger'

    @dashApp.callback(
        Output('container', 'children'),
        [Input('route', 'pathname')]
    )
    def navigation(pathname):
        if pathname == '/':
            return initialize_home_page(general_statistics, ontology_figures, triples_count)
        elif pathname == '/about':
            return initialize_about_page()

    @dashApp.callback(
        Output('ontology', 'figure'),
        [Input('btn_ontologies', 'n_clicks')]
    )
    def change_hierarchy(n_clicks):
        return ontology_figures[n_clicks % 2]

    @dashApp.callback(
        Output('parent_instances', 'children'),
        [Input('ontology', 'clickData')]
    )
    def update_parent_instances_bar(data):
        selected_class = 'owlThing'
        if data is not None:
            if 'entry' not in data['points'][0].keys() or data['points'][0]['label'] == data['points'][0]['entry']:
                selected_class = data['points'][0]['parent']
            else:
                selected_class = data['points'][0]['label']
        selected_ontology_data_labels = ontology_data[ontology_data['parents'] == selected_class]['labels']
        if selected_ontology_data_labels.empty:
            selected_ontology_data_labels = ontology_data[ontology_data['labels'] == selected_class]['labels']
        selected_all_instances_data = all_instances_count_data[all_instances_count_data['class'].isin(selected_ontology_data_labels)]
        selected_all_instances_data = selected_all_instances_data.sort_values(by='instancecount', ascending=False)
        if selected_all_instances_data.empty:
            selected_all_instances_data.append({'class': selected_class, 'instancecount': 0}, ignore_index=True)
            return html.Div('No Instances Count Found For Selected Class',
                            className='w-100 h-100 text-center text-white p-5')
        figure = LF.all_instances_count_plot(selected_all_instances_data)
        return dcc.Graph(id='parent_instances_bar', figure=figure)

    @dashApp.callback(
        Output('response-datatable-div', 'children'),
        [Input('sparql-query-input', 'value'),
         Input('run-query-button', 'n_clicks')]
    )
    def updated_clicked(query, run):
        if run is not None:
            if query is not None or query != '':
                print(query)
                table = LF.user_query(query)
                table = dash_table.DataTable(
                    id='response-datatable',
                    data=table.to_dict('records'),
                    columns=[{'id': c, 'name': c} for c in table.columns],
                    page_size=10,
                    style_cell={'textAlign': 'left', 'minWidth': '180px', 'padding': 10},
                )
                return table
        else:
            return ''
