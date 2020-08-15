import json
from os import path

import numpy as np
import pandas as pd

dataPath = 'data/v1'


def test_data():
    if path.exists(dataPath + '/Ontologies.csv'):
        ontologyData = pd.read_csv(dataPath + '/Ontologies.csv')
        assert ontologyData.iloc[0]['parents'] is np.nan and ontologyData.iloc[0]['labels'] is not np.nan

    if path.exists(dataPath + '/GeneralStatistics.json'):
        with open(dataPath + '/GeneralStatistics.json') as generalStatisticsJSON:
            assert json.load(generalStatisticsJSON)
