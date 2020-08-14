import dash_core_components as dcc
import dash_table
from dash.dependencies import Output, Input

import src.LayoutFigures as LF
from src.layouts.About import initializeAbout
from src.layouts.HomePage import initializeHomePage


def initializeCallbacks(dashApp):
    ontologyFigures = LF.ontologyHierarchy()
    instancesCountFigures = LF.instanceCount()
    generalStatistics = LF.generalStatistics()

    @dashApp.callback(
        Output('container', 'children'),
        [Input('route', 'pathname')]
    )
    def navigation(pathname):
        if pathname == '/':
            return initializeHomePage(generalStatistics, ontologyFigures, instancesCountFigures)
        elif pathname == '/about':
            return initializeAbout()

    @dashApp.callback(
        Output('ontology', 'figure'),
        [Input('btn_ontologies', 'n_clicks')]
    )
    def change_hierarchy(n_clicks):
        return ontologyFigures[n_clicks % 2]

    @dashApp.callback(
        [Output('subclasses_instances', 'children'),
         Output('parentclass_label', 'children')],
        [Input('parent_instances_bar', 'clickData')]
    )
    def subclassesPlots(data):
        if data is not None:
            label = data['points'][0]['label']
            print(label)
            return [dcc.Graph(figure=instancesCountFigures[label + '+Pie'])], \
                   [label + ' Class Instances']

    @dashApp.callback(
        Output('response-datatable-div', 'children'),
        [Input('sparql-query-input', 'value'),
         Input('run-query-button', 'n_clicks')]
    )
    def updated_clicked(query, run):
        if run is not None:
            if query is not None or query != '':
                print(query)
                table = LF.userQuery(query)
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

    # @dashApp.callback(
    #     Output[],
    #     [Input('download-button', 'n_clicks')]
    # )
    # def download_response(n_clicks):
    #     return send_file()
