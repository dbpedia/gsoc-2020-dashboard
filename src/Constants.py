ONTOLOGY_HIERARCHY = "select ?class ?subclass ?depth { ?subclass rdfs:subClassOf ?class . { select ?subclass (COUNT(?class)-1 AS ?depth) { ?subclass rdfs:subClassOf* ?class . ?class rdfs:subClassOf* owl:Thing . } } } ORDER BY ?depth ?class ?subclass"

INSTANCES_COUNT = "SELECT distinct ?class ?subclass count (distinct ?instance) as ?tier2count  WHERE {{ ?subclass rdfs:subClassOf ?class FILTER (?class in (dbo:Person, dbo:Organisation, dbo:Place, dbo:Work, dbo:Event)) } UNION { SELECT ?subclass ?class { VALUES (?subclass ?class){ (dbo:Person dbo:Person) (dbo:Organization dbo:Organization) (dbo:Place dbo:Place) (dbo:Work dbo:Work) (dbo:Event dbo:Event)}}} ?instance rdf:type/rdfs:subClassOf* ?subclass . } Group by ?class ?subclass ORDER by ?class"

GENERAL_STATISTICS = {
    "TOTAL_TRIPLES": "SELECT (COUNT(*) AS ?counts) WHERE { ?s ?p ?o }",
    "TOTAL_CLASSES": "SELECT (COUNT(DISTINCT ?o) AS ?counts) WHERE { ?s a ?o }",
    "TOTAL_PROPERTIES": "SELECT (COUNT(DISTINCT ?p) AS ?counts) WHERE { ?s ?p ?o }",
    "BLANK_SUBJECTS": "SELECT (COUNT(DISTINCT ?s) AS ?counts) WHERE { ?s ?p ?o FILTER(isBlank(?s))}",
    "BLANK_OBJECTS": "SELECT (COUNT(DISTINCT ?o ) AS ?counts) WHERE { ?s ?p ?o FILTER(isBlank(?o))}"
}
