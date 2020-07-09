import dash_core_components as dcc
from dash.dependencies import Output, Input

import src.LayoutFigures as LF


def initializeCallbacks(dashApp):
    ontologyHierarchyFigure = LF.ontologyHierarchy()
    instancesCountFigures = LF.instanceCount()

    @dashApp.callback(
        [Output('ontology_container', 'style'),
         Output('instances_count_container', 'style'),
         Output('ontology', 'children'),
         Output('parent_instances', 'children')],
        [Input('class_details', 'value')])
    def ontologySunburst(tabValue):
        if tabValue == 'ontology':
            print(tabValue)
            return {'display': 'block'}, {'display': 'none'}, [dcc.Graph(figure=ontologyHierarchyFigure)], []

        elif tabValue == 'instance_count':
            print(tabValue)
            return {'display': 'none'}, {'display': 'block'}, [], \
                   [dcc.Graph(id='parent_instances_bar', figure=instancesCountFigures['parent'])]

    @dashApp.callback(
        [Output('subclasses_instances', 'children'),
         Output('parentclass_label', 'children')],
        [Input('parent_instances_bar', 'clickData')]
    )
    def subclassesPlots(data):
        if data is not None:
            label = data['points'][0]['label']
            print(label)
            return [dcc.Graph(figure=instancesCountFigures[label + '+Pie'])], [label + ' Class Instances']
