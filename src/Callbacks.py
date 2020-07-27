import dash_core_components as dcc
from dash.dependencies import Output, Input, State

import src.LayoutFigures as LF
from src.layouts.About import initializeAbout
from src.layouts.HomePage import initializeHomePage
from src.layouts.InstancesCount import initializeInstancesCount
from src.layouts.Ontologies import initializeOntologies


def initializeCallbacks(dashApp):
    ontologyHierarchyFigure = LF.ontologyHierarchy()
    instancesCountFigures = LF.instanceCount()
    totalTriples = LF.totalTriples()
    totalClasses = LF.totalClasses()
    totalProperties = LF.totalProperties()

    @dashApp.callback(
        Output('container', 'children'),
        [Input('route', 'pathname')]
    )
    def button_action(pathname):
        if pathname == '/':
            print(pathname)
            return initializeHomePage(totalTriples, totalClasses, totalProperties)
        elif pathname == '/about':
            print(pathname)
            return initializeAbout()
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
