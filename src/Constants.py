ONTOLOGY_HIERARCHY = "select ?class ?subclass ?depth { ?subclass rdfs:subClassOf ?class . { select ?subclass (count(?class)-1 as ?depth) { ?subclass rdfs:subClassOf* ?class . ?class rdfs:subClassOf* owl:Thing . } } } order by ?depth ?class ?subclass"

SPECIFIC_INSTANCES_COUNT = "select distinct ?class ?subclass count (distinct ?instance) as ?tier2count  where {{ ?subclass rdfs:subClassOf ?class filter (?class in (dbo:Person, dbo:Organisation, dbo:Place, dbo:Work, dbo:Event)) } union { SELECT ?subclass ?class { VALUES (?subclass ?class){ (dbo:Person dbo:Person) (dbo:Organization dbo:Organization) (dbo:Place dbo:Place) (dbo:Work dbo:Work) (dbo:Event dbo:Event)}}} ?instance rdf:type/rdfs:subClassOf* ?subclass . } group by ?class ?subclass order by ?class"

ALL_INSTANCES_COUNT = "select ?class count(?s) as ?instancecount { ?s a ?class } group by ?class"

GENERAL_STATISTICS = {
    "TOTAL_TRIPLES": "select (count(*) as ?counts) where { ?s ?p ?o }",
    "TOTAL_CLASSES": "select (count(distinct ?o) as ?counts) where { ?s a ?o }",
    "TOTAL_PROPERTIES": "select (count(distinct ?p) as ?counts) where { ?s ?p ?o }",
    "BLANK_SUBJECTS": "select (count(distinct ?s) as ?counts) where { ?s ?p ?o filter(isBlank(?s))}",
    "BLANK_OBJECTS": "select (count(distinct ?o ) as ?counts) where { ?s ?p ?o filter(isBlank(?o))}"
}
