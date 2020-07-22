import dash_core_components as dcc
import dash_html_components as html


def initializeOntologies(ontologyHierarchyFigure):
    # plot ontology hierarchy graphs
    ontologies = html.Div(id='ontology_container', children=[
        dcc.Loading(id='ontology_loader', type='cube', className='h-100 align-items-center', children=[
            html.Div(id='ontology', children=[
                dcc.Graph(figure=ontologyHierarchyFigure)
            ])
        ])
    ], className='card w-100 bg-dark'),
    return ontologies
