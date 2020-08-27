import dash_core_components as dcc
import dash_table
from dash.dependencies import Output, Input

import src.LayoutFigures as LF
from src.layouts.About import initialize_about_page
from src.layouts.Home import initialize_home_page


def initialize_callbacks(dashApp):
    ontology_data, ontology_figures = LF.ontology_hierarchy()
    all_instances_count_data, all_instances_count_figure = LF.all_instances_count()
    general_statistics = LF.get_general_statistics()

    @dashApp.callback(
        Output('container', 'children'),
        [Input('route', 'pathname')]
    )
    def navigation(pathname):
        if pathname == '/':
            return initialize_home_page(general_statistics, ontology_figures)
        elif pathname == '/about':
            return initialize_about_page()

    @dashApp.callback(
        Output('ontology', 'figure'),
        [Input('btn_ontologies', 'n_clicks')]
    )
    def change_hierarchy(n_clicks):
        return ontology_figures[n_clicks % 2]

    @dashApp.callback(
        Output('parent_instances', 'children'),
        [Input('ontology', 'clickData')]
    )
    def update_parent_instances_bar(data):
        if data is not None:
            selected_class = data['points'][0]['label']
            selected_ontology_data_labels = ontology_data[ontology_data['parents'] == selected_class]['labels']
            selected_all_instances_data = all_instances_count_data[all_instances_count_data['class'].isin(selected_ontology_data_labels)]
            selected_all_instances_data = selected_all_instances_data.sort_values(by='instancecount', ascending=False)
            figure = LF.all_instances_count_plot(selected_all_instances_data)
            return dcc.Graph(id='parent_instances_bar', figure=figure)
        else:
            default_data_labels = ontology_data[ontology_data['parents'] == 'owlThing']['labels']
            selected_all_instances_data = all_instances_count_data[all_instances_count_data['class'].isin(default_data_labels)]
            selected_all_instances_data = selected_all_instances_data.sort_values(by='instancecount', ascending=False)
            figure = LF.all_instances_count_plot(selected_all_instances_data)
            return dcc.Graph(id='parent_instances_bar', figure=figure)

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
