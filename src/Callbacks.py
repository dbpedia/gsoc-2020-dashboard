import dash_core_components as dcc
from flask import send_file
from dash.dependencies import Output, Input

import src.LayoutFigures as LF
from src.layouts.About import initializeAbout
from src.layouts.HomePage import initializeHomePage


def initializeCallbacks(dashApp):
    ontologyFigures = LF.ontologyHierarchy()
    instancesCountFigures = LF.instanceCount()
    totalTriples = LF.totalTriples()
    totalClasses = LF.totalClasses()
    totalProperties = LF.totalProperties()
    blankSubjects = LF.blankSubjects()
    blankObjects = LF.blankObjects()

    @dashApp.callback(
        Output('container', 'children'),
        [Input('route', 'pathname')]
    )
    def navigation(pathname):
        if pathname == '/':
            return initializeHomePage(totalTriples, totalClasses, totalProperties,
                                      ontologyFigures, instancesCountFigures, blankSubjects, blankObjects)
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
        [Output('response-datatable', 'data'),
         Output('response-datatable', 'columns')],
        [Input('sparql-query-input', 'value'),
         Input('run-query-button', 'n_clicks')]
    )
    def updated_clicked(query, run):
        if run is not None:
            if query is not None or query != '':
                print(query)
                table = LF.userQuery(query)
                return table.to_dict('records'), [{'id': column, 'name': column} for column in table.columns]
        else:
            return dict(), list()


    # @dashApp.callback(
    #     Output[],
    #     [Input('download-button', 'n_clicks')]
    # )
    # def download_response(n_clicks):
    #     return send_file()
