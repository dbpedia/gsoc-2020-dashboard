from io import StringIO

import pandas as pd
import numpy as np

def to_specific_instance_count(csv_data):
    instances_count = pd.read_csv(StringIO(csv_data.decode("utf-8")), sep=',')

    instances_count['class'] = instances_count['class'].apply(lambda s: s[s.rindex('/') + 1:].replace('#', ''))
    instances_count['subclass'] = instances_count['subclass'].apply(lambda s: s[s.rindex('/') + 1:].replace('#', ''))

    parent_classes = instances_count.groupby(by='class', as_index=False).sum()

    return parent_classes, instances_count


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
