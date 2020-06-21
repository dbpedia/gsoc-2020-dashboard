import dash_core_components as dcc
from dash.dependencies import Output, Input

import src.LayoutFigures as LF


def initializeCallbacks(dashApp):
    @dashApp.callback(
        Output('ontology', 'children'),
        [Input('ontologies', 'value')])
    def ontologySunburst(tabname):
        if tabname == 'ontology-1':
            print(tabname)
            return [dcc.Graph(figure=LF.ontologyHierarchy())]
        elif tabname == 'ontology-2':
            print(tabname)
            return [dcc.Graph(figure=LF.instanceCount())]
