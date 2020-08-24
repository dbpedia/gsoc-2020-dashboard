import json
from os import path

import numpy as np
import pandas as pd

data_path = 'data/v1'


def test_datafiles():
    if path.exists(data_path + '/Ontologies.csv'):
        ontology_data = pd.read_csv(data_path + '/Ontologies.csv')
        assert ontology_data.iloc[0]['parents'] is np.nan and ontology_data.iloc[0]['labels'] is not np.nan

    if path.exists(data_path + '/GeneralStatistics.json'):
        with open(data_path + '/GeneralStatistics.json') as generalStatisticsJSON:
            assert json.load(generalStatisticsJSON)
