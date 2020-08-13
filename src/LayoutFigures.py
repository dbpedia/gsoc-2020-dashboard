from SPARQLWrapper import JSON, CSV
from os import path
import pandas as pd
import src.CSVParser as CSVP
import src.JSONParser as JP
import src.RequestData as RD
import src.Visualize as VI

dataPath = 'data/v1'

def ontologyHierarchy():
    ontologyData = ''
    if path.exists(dataPath + '/Ontologies.csv'):
        ontologyData = pd.read_csv(dataPath + '/Ontologies.csv')
        print('ontologies fetched from the file')
    else:
        results = RD.sparqlWrapper(
            "select ?class ?subclass ?depth { ?subclass rdfs:subClassOf ?class . { select ?subclass (COUNT(?class)-1 AS ?depth) { ?subclass rdfs:subClassOf* ?class . ?class rdfs:subClassOf* owl:Thing . } } } ORDER BY ?depth ?class ?subclass",
            JSON)
        ontologyData = JP.toOntologyHierarchy(results)
        ontologyData.to_csv('data/v1/Ontologies.csv', index=False, index_label=False)
    return VI.ontologySunburst(ontologyData)


def instanceCount():
    parentClasses, instancesCount = '', ''
    if path.exists(dataPath + '/instancesCount.csv') and path.exists(dataPath + '/parentClasses.csv'):
        parentClasses = pd.read_csv(dataPath + '/parentClasses.csv')
        instancesCount = pd.read_csv(dataPath + '/instancesCount.csv')
        print('instances fetched from the file')
    else:
        results = RD.sparqlWrapper(
            "SELECT distinct ?class ?subclass count (distinct ?instance) as ?tier2count  WHERE {{ ?subclass rdfs:subClassOf ?class FILTER (?class in (dbo:Person, dbo:Organisation, dbo:Place, dbo:Work, dbo:Event)) } UNION { SELECT ?subclass ?class { VALUES (?subclass ?class){ (dbo:Person dbo:Person) (dbo:Organization dbo:Organization) (dbo:Place dbo:Place) (dbo:Work dbo:Work) (dbo:Event dbo:Event)}}} ?instance rdf:type/rdfs:subClassOf* ?subclass . } Group by ?class ?subclass ORDER by ?class",
            CSV)
        parentClasses, instancesCount = CSVP.toInstanceCount(results)
        parentClasses.to_csv('data/v1/parentClasses.csv', index_label=False, index=False)
        instancesCount.to_csv('data/v1/instancesCount.csv', index_label=False, index=False)
    return VI.instanceCountBar(parentClasses, instancesCount)


def totalTriples():
    results = RD.sparqlWrapper(
        "SELECT (COUNT(*) AS ?x) WHERE { ?s ?p ?o }",
        CSV)
    totalTriples = CSVP.parseCounts(results)
    return str(totalTriples.iloc[0]['x'])


def totalClasses():
    results = RD.sparqlWrapper(
        "SELECT (COUNT(DISTINCT ?o) AS ?x) WHERE { ?s a ?o }",
        CSV
    )
    totalClasses = CSVP.parseCounts(results)
    return str(totalClasses.iloc[0]['x'])


def totalProperties():
    results = RD.sparqlWrapper(
        "SELECT (COUNT(DISTINCT ?p) AS ?x) WHERE { ?s ?p ?o }",
        CSV
    )
    totalProperties = CSVP.parseCounts(results)
    return str(totalProperties.iloc[0]['x'])


def blankSubjects():
    results = RD.sparqlWrapper(
        "SELECT (COUNT(DISTINCT ?s) AS ?x) WHERE { ?s ?p ?o FILTER(isBlank(?s))}",
        CSV
    )
    blankSubjects = CSVP.parseCounts(results)
    return str(blankSubjects.iloc[0]['x'])


def blankObjects():
    results = RD.sparqlWrapper(
        "SELECT (COUNT(DISTINCT ?o ) AS ?x) WHERE { ?s ?p ?o FILTER(isBlank(?o))}",
        CSV
    )
    blankSubjects = CSVP.parseCounts(results)
    return str(blankSubjects.iloc[0]['x'])


def userQuery(query):
    results = RD.sparqlWrapper(
        query, CSV
    )
    table = CSVP.parseQueryResponse(results)
    return table
