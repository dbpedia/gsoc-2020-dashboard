# Google Summer of Code 2020 Dashboard

Currently, DBpedia holds huge amount of data and latest-core gets updated regularly.
So, it is important to know the statistics of these cores.

Dashboard URL: http://78.46.100.7:9000/

Proposal: [Dashboard for Language/National Knowledge Graphs](https://drive.google.com/file/d/128tpjrR60Ag13qLKgz0j4Daq703fnofD/view?usp=sharing)

## Problem:
Due to huge amount of data, it is difficult to maintain the quality and on the other hand it is also critical to know the statistics of the data core. Most of the users and community members may find the task of summarizing the data tiresome as this summary of data varies user by user. Though, there are some basic statistics that can help in getting knowledge of the data core by querying the SPARQL endpoint. However, getting these data programatically or in the tabular form is not appropriate for performing the analysis for quality assessment. Based on SPARQL queries, result sets may get huge which is eventually of no use because of the nature of format.

## Solution:
In order to get everything on single platform where users can query, visualize, and get knowledge of current data core, a centralized system (dashboard) is useful. This dashboard is the platform that shows key metrics or key performance indicator (KPI) of instances, properties, classes and their subclasses. In addition to this, feature of performing comparison between several classes is also introduced. The first step in designing this system includes visualizing the hierarchy (ontologies) in a way that it shows the instances count proportion of each class and subclass. Several visualizations like sunburst and treemap are used for this displaying the instances count proportion.

![sunburst of ontologies hierarchy of latest-core](https://github.com/dbpedia/gsoc-2020-dashboard/blob/master/wiki/sunburst.png)

Moreover, to increase the user interactivity, horizontal bar chart is also plotted that has the functionality of plotting sub-charts when bars are clicked. At present, this dashboard contains above mentioned visualizations. The home page has another functionality where users can run the SPARQL queries on different cores and specify the format, and execution timeout along with download feature. Once, the query is executed successfully, the response will be displayed in tabular form with appropriate user interface and pagination. Currently, only CSV format is working. However, the functionality to "download" and specify "core-version" is not yet implemented, but will be implemented soon.

![home page general statistics](https://raw.githubusercontent.com/dbpedia/gsoc-2020-dashboard/master/wiki/homepage.png)

In the below image, horizontal bar chart is displayed. The bars that are visualized are those classes that holds the highest number of instances in the latest core. Clicking on the 5 bars will generate the sub-chart based on the selected bar (class). The sub-chart represents the instances count of the selected parent class.

![instances count](https://raw.githubusercontent.com/dbpedia/gsoc-2020-dashboard/master/wiki/instancescount.png)

## Development Life Cycle:
Tools and Frameworks used for developing this system:
1) [Flask](https://flask.palletsprojects.com/en/1.1.x/) framework (for backend operations and handling requests)
2) [Docker](https://www.docker.com/) (for deployment)
3) [Plotly](https://plotly.com/) and [D3.js](https://d3js.org/) (for visualizations)
4) [Jetbrains IDE PyCharm](https://www.jetbrains.com/pycharm/) (for efficient development and continous integration)

This dashboard is currently deployed on DBpedia's server using docker. On the same server, [dockerized-dbpedia](https://github.com/dbpedia/Dockerized-DBpedia) that contains the latest-core is also running, which eventually acts as SPARQL endpoint for executing the query. When new commits are made to this repository, docker image is built on the docker hub. This updated docker image is then pulled on DBpedia's server to update the live dashboard.

## Running on your local system:

In order to run this project in local system, the best recommended IDE to use is PyCharm and follow the below steps.
1) Clone the repository using PyCharm's feature of "Import from version control".
2) After cloning, setup the virtual environment and run "pip install -r requirements.txt". This step will install all the dependencies in the virtual environment.
3) Lastly, run the "app.py" python file and open the browser. By default, application will run on localhost.
