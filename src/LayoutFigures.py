import src.JSONParser as JP
import src.RequestData as RD
import src.Visualize as VI
import json

def ontologyHierarchy():
    results = RD.sparqlWrapper(
        "select ?class ?subclass ?depth { ?subclass rdfs:subClassOf ?class . { select ?subclass (COUNT(?class)-1 AS ?depth) { ?subclass rdfs:subClassOf* ?class . ?class rdfs:subClassOf* owl:Thing . } } } ORDER BY ?depth ?class ?subclass")
    ontologyData = JP.toOntologyHierarchy(results)
    return VI.ontologySunburst(ontologyData)


def instanceCount(classNames):
    with open('data/InstanceCounts.json', 'r') as f:
        # results = RD.sparqlWrapper(
        #     "SELECT distinct ?class ?subclass count (distinct ?instance) as ?tier2count  WHERE {{ ?subclass rdfs:subClassOf ?class FILTER (?class in (dbo:Person, dbo:Organisation, dbo:Place, dbo:Work, dbo:Event)) } UNION { SELECT ?subclass ?class { VALUES (?subclass ?class){ (dbo:Person dbo:Person) }}} ?instance rdf:type/rdfs:subClassOf* ?subclass . } Group by ?class ?subclass ORDER by ?class")
        results = json.load(f)
        instancesData = JP.toInstanceCount(results)
        return VI.instanceCountPolar(instancesData, classNames)

