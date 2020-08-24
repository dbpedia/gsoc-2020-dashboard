from SPARQLWrapper import SPARQLWrapper


def sparql_wrapper(query, response_format):
    sparql = SPARQLWrapper("http://78.46.100.7:8890/sparql")

    sparql.setQuery(query=query)
    sparql.setReturnFormat(response_format)

    print("fetching results...")
    results = sparql.query().convert()
    return results
