import dash_core_components as dcc
from dash.dependencies import Output, Input

import src.LayoutFigures as LF


def initializeCallbacks(dashApp):
    @dashApp.callback(
        Output('ontology', 'children'),
        [Input('class_details', 'value')])
    def ontologySunburst(tabname):
        if tabname == 'ontology':
            print(tabname)
            return [dcc.Graph(figure=LF.ontologyHierarchy())]
        elif tabname == 'instance_count':
            print(tabname)
            return [dcc.Graph(figure=LF.instanceCount())]
