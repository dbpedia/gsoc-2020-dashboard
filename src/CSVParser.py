from io import StringIO

import pandas as pd


def toInstanceCount(csv_data):
    instancesCount = pd.read_csv(StringIO(csv_data.decode("utf-8")), sep=',')

    instancesCount['class'] = instancesCount['class'].apply(lambda s: s[s.rindex('/') + 1:].replace('#', ''))
    instancesCount['subclass'] = instancesCount['subclass'].apply(lambda s: s[s.rindex('/') + 1:].replace('#', ''))

    print(instancesCount)

    parentClasses = instancesCount.groupby(by='class', as_index=False).sum()
    print(parentClasses)

    return parentClasses, instancesCount


def parseCounts(csv_data):
    totalTriples = pd.read_csv(StringIO(csv_data.decode("utf-8")), sep=',')
    return totalTriples


def parseQueryResponse(csv_data):
    table = pd.read_csv(StringIO(csv_data.decode("utf-8")), sep=',')
    return table
