import pandas as pd


def to_ontology_hierarchy(json_data):
    superclasses, subclasses = list(), list()
    superclasses.append('')
    subclasses.append('owlThing')
    top_level = list()

    for row in json_data['results']['bindings']:

        # get class link
        superclass = str(row['class']['value'])
        subclass = str(row['subclass']['value'])

        # fetch class name
        superclass = superclass[superclass.rindex('/') + 1:].replace('#', '')
        subclass = subclass[subclass.rindex('/') + 1:].replace('#', '')

        if 'owlThing' in superclass:
            top_level.append(subclass)
            superclasses.append(superclass)
            subclasses.append(subclass)
        elif superclass in top_level or superclass in subclasses:
            superclasses.append(superclass)
            subclasses.append(subclass)

    ontology_data_frame = pd.DataFrame()
    ontology_data_frame['parents'] = pd.Series(superclasses)
    ontology_data_frame['labels'] = pd.Series(subclasses)
    return ontology_data_frame
