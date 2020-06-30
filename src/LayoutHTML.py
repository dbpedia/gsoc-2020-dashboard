import dash_core_components as dcc
import dash_html_components as html


def homePageLayout(dashApp):
    dashApp.layout = html.Div([

        dcc.Location(id='url', refresh=False),

        # tabs
        dcc.Tabs(id='class_details', value='ontology', children=[
            dcc.Tab(label='Ontology Sunburst', value='ontology'),
            dcc.Tab(label='Instances Count', value='instance_count')
        ], colors={
            "border": "#212121",
            "primary": "#212121",
            "background": "#9E9E9E"
        }),

        # tidy tree
        # html.Div([
        #     dcc.Loading(id='tidy_tree_loader', type='cube', className='h-100 align-items-center', children=[
        #         html.Iframe(src='../assets/radial.html', style={'background': '#FFFFFF', 'width': 1500, 'height':1500}),
        #     ])
        # ], className='card w-100 bg-dark'),

        # plot ontology hierarchy graphs
        html.Div(id='ontology_container', children=[
            dcc.Loading(id='ontology_loader', type='cube', className='h-100 align-items-center', children=[
                html.Div(id='ontology')
            ])
        ], className='card w-100 bg-dark'),

        # plot instance count graphs
        html.Div(id='instances_count_container', children=[
            html.Div([
                # event
                html.Div([
                    html.Div([
                        html.Div([
                            dcc.Loading(id='instances_event_loader', type='cube',
                                        className='h-100 align-items-center',
                                        children=[
                                            html.Div(id='instances_event')
                                        ])
                        ], className='card-body', style={'padding': 0, 'border-radius': '12px'})
                    ], className='card bg-dark')
                ], className='col'),
                # person
                # html.Div([
                #     html.Div([
                #         html.Div([
                #             dcc.Loading(id='instances_person_loader', type='cube',
                #                         className='h-100 align-items-center',
                #                         children=[
                #                             html.Div(id='instances_person')
                #                         ])
                #         ], className='card-body', style={'padding': 0, 'border-radius': '12px'})
                #     ], className='card bg-dark')
                # ], className='col'),
                # organisation
                # html.Div([
                #     html.Div([
                #         html.Div([
                #             dcc.Loading(id='instances_organisation_loader', type='cube',
                #                         className='h-100 align-items-center',
                #                         children=[
                #                             html.Div(id='instances_organisation')
                #                         ])
                #         ], className='card-body', style={'padding': 0, 'border-radius': '12px'})
                #     ], className='card bg-dark')
                # ], className='col')

            ], className='row'),

            # html.Div([
            #     #work
            #     html.Div([
            #         html.Div([
            #             html.Div([
            #                 dcc.Loading(id='instances_work_loader', type='cube',
            #                             className='h-100 align-items-center',
            #                             children=[
            #                                 html.Div(id='instances_work')
            #                             ])
            #             ], className='card-body', style={'padding': 0, 'border-radius': '12px'})
            #         ], className='card bg-dark')
            #     ], className='col'),
            #
            #     #place
            #     html.Div([
            #         html.Div([
            #             html.Div([
            #                 dcc.Loading(id='instances_place_loader', type='cube',
            #                             className='h-100 align-items-center',
            #                             children=[
            #                                 html.Div(id='instances_place')
            #                             ])
            #             ], className='card-body', style={'padding': 0, 'border-radius': '12px'})
            #         ], className='card bg-dark')
            #     ], className='col')
            #
            # ], className='row')

        ], className='w-100 bg-dark', style={'display': 'none'})

    ], className='w-100')
