from SPARQLWrapper import SPARQLWrapper, JSON
import requests


def sparqlWrapper(query):
    sparql = SPARQLWrapper("https://dbpedia.org/sparql")

    sparql.setQuery(query=query)
    sparql.setReturnFormat(JSON)
    sparql.addDefaultGraph("http://dbpedia.org")

    print("fetching results...")
    results = sparql.query().convert()
    return results
