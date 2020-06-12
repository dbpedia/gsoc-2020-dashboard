from SPARQLWrapper import SPARQLWrapper, JSON


def sparqlWrapper(query):
    print("requesting..")
    # query = "select ?class count(?s) as ?scount {?s a ?class} group by ?class order by desc(?scount) limit 5"
    sparql = SPARQLWrapper("https://dbpedia.org/sparql")

    sparql.setQuery(query=query)
    sparql.setReturnFormat(JSON)
    sparql.addDefaultGraph("http://dbpedia.org")

    results = sparql.query().convert()
    return results
