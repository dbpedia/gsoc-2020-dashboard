import os

import dash

import src.Callbacks as CB
import src.layouts.ParentLayout as LHTML

global dash_app


def initialize_dash_app():
    global dash_app
    dash_app = dash.Dash(__name__,
                         meta_tags=[{"name": "viewport", "content": "width=1024"}],
                         external_stylesheets=['https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'])
    app_server = dash_app.server

    dash_app.title = 'DBpedia Dashboard'

    # initialize all layouts
    LHTML.root_layout(dash_app)

    return app_server, dash_app


if __name__ == '__main__':
    app_server, dash_app = initialize_dash_app()
    CB.initialize_callbacks(dash_app)
    dash_app.run_server(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
