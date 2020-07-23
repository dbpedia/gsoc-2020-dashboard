import os
import dash
import src.Callbacks as CB
import src.ParentLayout as LHTML

global dashApp


def initializeDashApp():
    global dashApp
    dashApp = dash.Dash(__name__,
                        meta_tags=[{"name": "viewport", "content": "width=1024"}],
                        external_scripts=['https://d3js.org/d3.v5.min.js'],
                        external_stylesheets=[
                            'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'])
    app = dashApp.server
    dashApp.title = 'DBpedia Dashboard'

    # initialize all layouts
    LHTML.homePageLayout(dashApp)

    return app, dashApp


if __name__ == '__main__':
    app, dashApp = initializeDashApp()
    CB.initializeCallbacks(dashApp)
    dashApp.run_server(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
