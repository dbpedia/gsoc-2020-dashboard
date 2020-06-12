import dash_core_components as dcc
import dash_html_components as html

import src.LayoutFigures as LF


def homePageLayout(dashApp):
    dashApp.layout = html.Div([

        # plot ontology hierarchy sunburst
        dcc.Graph(figure=LF.ontologyHierarchy())

    ])
