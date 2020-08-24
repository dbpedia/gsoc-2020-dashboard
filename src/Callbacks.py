import dash_core_components as dcc
import dash_table
from dash.dependencies import Output, Input

import src.LayoutFigures as LF
from src.layouts.About import initialize_about_page
from src.layouts.Home import initialize_home_page


def initialize_callbacks(dashApp):
    ontology_figures = LF.ontology_hierarchy()
    instances_count_figures = LF.instance_count()
    general_statistics = LF.get_general_statistics()

    @dashApp.callback(
        Output('container', 'children'),
        [Input('route', 'pathname')]
    )
    def navigation(pathname):
        if pathname == '/':
            return initialize_home_page(general_statistics, ontology_figures, instances_count_figures)
        elif pathname == '/about':
            return initialize_about_page()

    @dashApp.callback(
        Output('ontology', 'figure'),
        [Input('btn_ontologies', 'n_clicks')]
    )
    def change_hierarchy(n_clicks):
        return ontology_figures[n_clicks % 2]

    @dashApp.callback(
        [Output('subclasses_instances', 'children'),
         Output('parentclass_label', 'children')],
        [Input('parent_instances_bar', 'clickData')]
    )
    def subclasses_plots(data):
        if data is not None:
            label = data['points'][0]['label']
            print(label)
            return [dcc.Graph(figure=instances_count_figures[label + '+Pie'])], \
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

    # @dashApp.callback(
    #     Output[],
    #     [Input('download-button', 'n_clicks')]
    # )
    # def download_response(n_clicks):
    #     return send_file()
