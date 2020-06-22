import dash_core_components as dcc
from dash.dependencies import Output, Input

import src.LayoutFigures as LF


def initializeCallbacks(dashApp):
    @dashApp.callback(
        [Output('ontology_container', 'style'),
         Output('instance_count_container', 'style'),
         Output('ontology', 'children'),
         Output('instance_count', 'children')],
        [Input('class_details', 'value')])
    def ontologySunburst(tabname):
        if tabname == 'ontology':
            print(tabname)
            return {'display': 'block'}, {'display': 'none'}, [dcc.Graph(figure=LF.ontologyHierarchy())], []
        elif tabname == 'instance_count':
            print(tabname)
            return {'display': 'none'}, {'display': 'block'}, [], [dcc.Graph(figure=LF.instanceCount())]
