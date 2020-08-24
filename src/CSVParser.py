from io import StringIO

import pandas as pd


def to_instance_count(csv_data):
    instances_count = pd.read_csv(StringIO(csv_data.decode("utf-8")), sep=',')

    instances_count['class'] = instances_count['class'].apply(lambda s: s[s.rindex('/') + 1:].replace('#', ''))
    instances_count['subclass'] = instances_count['subclass'].apply(lambda s: s[s.rindex('/') + 1:].replace('#', ''))

    parent_classes = instances_count.groupby(by='class', as_index=False).sum()

    return parent_classes, instances_count


def parse_query_response(csv_data):
    table = pd.read_csv(StringIO(csv_data.decode("utf-8")), sep=',')
    return table
