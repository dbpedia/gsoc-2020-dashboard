import dash_core_components as dcc
from dash.dependencies import Output, Input, State

import src.LayoutFigures as LF
from src.layouts.InstancesCount import initializeInstancesCount
from src.layouts.Ontologies import initializeOntologies
from src.layouts.HomePage import initializeHomePage


def initializeCallbacks(dashApp):
    ontologyHierarchyFigure = LF.ontologyHierarchy()
    # instancesCountFigures = LF.instanceCount()

    @dashApp.callback(
        Output('container', 'children'),
        [Input('route', 'pathname')]
    )
    def button_action(pathname):
        if pathname == '/':
            print(pathname)
            return initializeHomePage()
        elif pathname == '/ontologies':
            print(pathname)
            return initializeOntologies(ontologyHierarchyFigure)
        elif pathname == '/instancescount':
            print(pathname)
            return initializeInstancesCount(instancesCountFigures)

    @dashApp.callback(
        Output('route', 'pathname'),
        [Input('clicked-button', 'children')]
    )
    def button_action(clicked):
        idx = clicked.rfind(':') + 1
        clicked = clicked[idx:]
        print(clicked)
        if clicked == 'ontologies':
            return '/ontologies'
        if clicked == 'instancescount':
            return '/instancescount'

    @dashApp.callback(
        Output('clicked-button', 'children'),
        [Input('btn_ontologies', 'n_clicks'),
         Input('btn_instancescount', 'n_clicks')],
        [State('clicked-button', 'children')]
    )
    def updated_clicked(btn_ontologies_click, btn_instancescount_click, prev_clicks):
        prev_clicks = dict([i.split(':') for i in prev_clicks.split(' ')])
        last_clicked = 'nan'

        if btn_ontologies_click > int(prev_clicks['ontologies']):
            last_clicked = 'ontologies'
        elif btn_instancescount_click > int(prev_clicks['instancescount']):
            last_clicked = 'instancescount'

        cur_clicks = 'ontologies:{} instancescount:{} last:{}'.format(btn_ontologies_click, btn_instancescount_click,
                                                                      last_clicked)
        return cur_clicks

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
