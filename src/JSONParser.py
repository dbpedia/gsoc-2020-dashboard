import pandas as pd





def toOntologyHierarchy(json_data):
    superClasses = list()
    subClasses = list()
    topLevel = list()

    for row in json_data['results']['bindings']:

        # get class link
        superClass = str(row['class']['value'])
        subClass = str(row['subclass']['value'])

        # fetch class name
        superClass = superClass[superClass.rindex("/") + 1:].replace("#", "")
        subClass = subClass[subClass.rindex("/") + 1:].replace("#", "")

        if 'owlThing' in superClass:
            topLevel.append(subClass)
            superClasses.append(superClass)
            subClasses.append(subClass)
        elif superClass in topLevel or superClass in subClasses:
            superClasses.append(superClass)
            subClasses.append(subClass)

    return (superClasses, subClasses)


def toInstanceCount(json_data):
    instanceName = list()
    instanceCount = list()

    for row in json_data['results']['bindings']:
        if "dbpedia.org/ontology" in row['class']['value']:
            # get class link
            classValue = str(row['class']['value'])
            classValue = classValue[classValue.rindex("/") + 1:]

            instanceCountValue = str(row['instancecount']['value'])
            instanceName.append(classValue)
            instanceCount.append(instanceCountValue)

    return (instanceName, instanceCount)
