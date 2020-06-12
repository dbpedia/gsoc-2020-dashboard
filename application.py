import src.DashInitialization as DI

if __name__ == '__main__':
    app, dashApp = DI.initializeDashApp()

    dashApp.run_server()
