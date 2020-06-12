import src.DashInitialization as DI
import os

if __name__ == '__main__':
    app, dashApp = DI.initializeDashApp()

    dashApp.run_server(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
