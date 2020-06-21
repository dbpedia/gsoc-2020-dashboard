import src.JSONParser as JP
import src.RequestData as RD
import src.Visualize as VI


def ontologyHierarchy():
    results = RD.sparqlWrapper(
        "select ?class ?subclass ?depth { ?subclass rdfs:subClassOf ?class . { select ?subclass (COUNT(?class)-1 AS ?depth) { ?subclass rdfs:subClassOf* ?class . ?class rdfs:subClassOf* owl:Thing . } } } ORDER BY ?depth ?class ?subclass")
    ontologyData = JP.toOntologyHierarchy(results)
    return VI.ontologySunburst(ontologyData)


def instanceCount():
    results = RD.sparqlWrapper(
        "select ?class count(?s) as ?instancecount {?s a ?class} group by ?class order by desc(?instancecount)")
    instancesData = JP.toInstanceCount(results)
    return VI.instanceCountPolar(instancesData)
