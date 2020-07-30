import dash_html_components as html


def initializeAbout():
    introduction_content = 'DBpedia dashboard is the project developed by Google Summer of Code student developer Karan Kharecha.'
    problem_statement = 'Due to huge amount of data, it is difficult to maintain the quality and on the other hand it is ' \
                        'also critical to know the statistics of the data core. Most of the users and community members ' \
                        'may find the task of summarizing the data tiresome as this summary of data varies user by user. ' \
                        'Though, there are some basic statistics that can help in getting knowledge of the data core by ' \
                        'querying the SPARQL endpoint. However, getting these data programatically or in the tabular ' \
                        'form is not appropriate for performing the analysis for quality assessment. Based on SPARQL ' \
                        'queries, result sets may get huge which is eventually of no use because of the nature of format.'
    solution_statement = 'In order to get everything on single platform where users can query, visualize, and get ' \
                         'knowledge of current data core, a centralized system (dashboard) is useful. This dashboard is ' \
                         'the platform that shows key metrics or key performance indicator (KPI) of instances, ' \
                         'properties, classes and their subclasses. In addition to this, feature of performing ' \
                         'comparison between several classes is also introduced. The first step in designing this system' \
                         ' includes visualizing the hierarchy (ontologies) in a way that it shows the instances count ' \
                         'proportion of each class and subclass. Several visualizations like sunburst and treemap are ' \
                         'used for this displaying the instances count proportion. \n Moreover, to increase the user ' \
                         'interactivity, horizontal bar chart is also plotted that has the functionality of plotting ' \
                         'sub-charts when bars are clicked. At present, this dashboard contains above mentioned ' \
                         'visualizations. The home page has another functionality where users can run the SPARQL queries' \
                         ' on different cores and specify the format, and execution timeout along with download feature.' \
                         ' Once, the query is executed successfully, the response will be displayed in tabular form with' \
                         ' appropriate user interface and pagination. Currently, only CSV format is working. However, ' \
                         'the functionality to "download" and specify "core-version" is not yet implemented, but will be' \
                         ' implemented soon.'

    about = html.Div(id='about_container', children=[

        html.Div([
            html.Div([
                html.Div([
                    html.P(id='introduction_content',
                           children=introduction_content,
                           className='about_content'),
                    html.H3(id='problem_heading',
                            children='Problem',
                            className='about_content'),
                    html.P(id='problem_content',
                           children=problem_statement,
                           className='about_content'),
                    html.H3(id='solution_heading',
                            children='Solution',
                            className='about_content'),
                    html.P(id='solution_content',
                           children=solution_statement,
                           className='about_content'),
                ], className='card-body')
            ], className='card')
        ], className='col'),

    ], className='w-100 row mt-5 p-0 text-center')

    return about
