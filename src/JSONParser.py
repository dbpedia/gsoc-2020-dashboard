def toClassesAndSubclasses(json_data):
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
