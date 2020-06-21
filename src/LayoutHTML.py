import dash_core_components as dcc
import dash_html_components as html


def homePageLayout(dashApp):
    dashApp.layout = html.Div([

        dcc.Location(id='url', refresh=False),

        # tabs
        dcc.Tabs(id='ontologies', value='ontology-1', children=[
            dcc.Tab(label='Ontology Sunburst', value='ontology-1'),
            dcc.Tab(label='Ontology Instance Count', value='ontology-2')
        ], colors={
            "border": "#212121",
            "primary": "#212121",
            "background": "#9E9E9E"
        }),

        # plot ontology hierarchy graphs
        html.Div([
            dcc.Loading(id='ontology_loader', type='cube', className='h-100 align-items-center', children=[
                html.Div(id='ontology')
            ])
        ], className='card w-100 bg-dark')

    ], className='w-100')
