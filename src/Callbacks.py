import dash_core_components as dcc
from dash.dependencies import Output, Input

import src.LayoutFigures as LF


def initializeCallbacks(dashApp):
    @dashApp.callback(
        [Output('ontology_container', 'style'),
         Output('instances_count_container', 'style'),
         Output('ontology', 'children'),
         Output('instances_event', 'children'),
         Output('instances_person', 'children'),
         Output('instances_organisation', 'children'),
         Output('instances_work', 'children'),
         Output('instances_place', 'children')],
        [Input('class_details', 'value')])
    def ontologySunburst(tabname):
        if tabname == 'ontology':
            print(tabname)
            return {'display': 'block'}, {'display': 'none'}, [dcc.Graph(figure=LF.ontologyHierarchy())], \
                   [], [], [], [], []

        elif tabname == 'instance_count':
            print(tabname)
            figures = LF.instanceCount(['Event', 'Person', 'Organisation', 'Work', 'Place'])
            return {'display': 'none'}, {'display': 'block'}, [], \
                   [dcc.Graph(figure=figures[0])], \
                   [dcc.Graph(figure=figures[1])], \
                   [dcc.Graph(figure=figures[2])], \
                   [dcc.Graph(figure=figures[3])], \
                   [dcc.Graph(figure=figures[4])]
