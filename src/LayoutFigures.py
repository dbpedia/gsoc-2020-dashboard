import src.JSONParser as JP
import src.RequestData as RD
import src.Visualize as VI


def ontologyHierarchy():
    results = RD.sparqlWrapper(
        "SELECT ?class ?subclass ?depth { ?subclass rdfs:subClassOf ?class . { SELECT ?subclass (COUNT(?class)-1 AS ?depth) { ?subclass rdfs:subClassOf* ?class . ?class rdfs:subClassOf* owl:Thing . } } } ORDER BY ?depth ?class ?subclass")
    ontologyData = JP.toClassesAndSubclasses(results)
    return VI.ontologySunburst(ontologyData)
