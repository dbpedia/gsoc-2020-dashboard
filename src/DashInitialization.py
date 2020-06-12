import dash
import src.LayoutHTML as LHTML


def initializeDashApp():
    dashApp = dash.Dash(__name__,
                        meta_tags=[{"name": "viewport", "content": "width=1024"}],
                        external_stylesheets=[
                            'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'])
    app = dashApp.server
    dashApp.title = 'DBpedia Dashboard'

    # initialize all layouts
    LHTML.homePageLayout(dashApp)

    return app, dashApp
