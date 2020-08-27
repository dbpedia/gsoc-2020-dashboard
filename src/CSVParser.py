from io import StringIO

import numpy as np
import pandas as pd


def extract_class_name(class_name):
    if 'dbpedia.org/ontology' in class_name:
        class_name = class_name[class_name.rindex('/') + 1:].replace('#', '')
        return class_name
    else:
        return np.nan


def to_all_instances_count(csv_data):
    table = pd.read_csv(StringIO(csv_data.decode("utf-8")), sep=',')
    table['class'] = table['class'].apply(lambda class_name: extract_class_name(str(class_name)))
    table = table[table['class'].notna()]
    return table


def parse_query_response(csv_data):
    table = pd.read_csv(StringIO(csv_data.decode("utf-8")), sep=',')
    return table
