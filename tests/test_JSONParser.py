import json

import src.JSONParser as JP


def test_to_ontology_hierarchy():
    with open('tests/mocks/Ontologies') as mock_ontologies:
        mock_json = json.load(mock_ontologies)
        data = JP.to_ontology_hierarchy(mock_json)
        assert data is not None and not data.empty
