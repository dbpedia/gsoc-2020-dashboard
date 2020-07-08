from SPARQLWrapper import JSON, CSV

import src.CSVParser as CSVP
import src.JSONParser as JP
import src.RequestData as RD
import src.Visualize as VI


def ontologyHierarchy():
    results = RD.sparqlWrapper(
        "select ?class ?subclass ?depth { ?subclass rdfs:subClassOf ?class . { select ?subclass (COUNT(?class)-1 AS ?depth) { ?subclass rdfs:subClassOf* ?class . ?class rdfs:subClassOf* owl:Thing . } } } ORDER BY ?depth ?class ?subclass",
        JSON)
    ontologyData = JP.toOntologyHierarchy(results)
    return VI.ontologySunburst(ontologyData)


def instanceCount():
    results = RD.sparqlWrapper(
        "SELECT distinct ?class ?subclass count (distinct ?instance) as ?tier2count  WHERE {{ ?subclass rdfs:subClassOf ?class FILTER (?class in (dbo:Person, dbo:Organisation, dbo:Place, dbo:Work, dbo:Event)) } UNION { SELECT ?subclass ?class { VALUES (?subclass ?class){ (dbo:Person dbo:Person) (dbo:Organization dbo:Organization) (dbo:Place dbo:Place) (dbo:Work dbo:Work) (dbo:Event dbo:Event)}}} ?instance rdf:type/rdfs:subClassOf* ?subclass . } Group by ?class ?subclass ORDER by ?class",
        CSV)
    parentClasses, instancesCount = CSVP.toInstanceCount(results)
    return VI.instanceCountBar(parentClasses, instancesCount)
