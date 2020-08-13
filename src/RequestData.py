from SPARQLWrapper import SPARQLWrapper, JSON, CSV


def sparqlWrapper(query, format):
    # checking
    # sparql = SPARQLWrapper("https://dbpedia.org/sparql")
    sparql = SPARQLWrapper("http://78.46.100.7:8890/sparql")

    sparql.setQuery(query=query)
    sparql.setReturnFormat(format)
    # sparql.addDefaultGraph("http://dbpedia.org")

    print("fetching results...")
    results = sparql.query().convert()
    return results
