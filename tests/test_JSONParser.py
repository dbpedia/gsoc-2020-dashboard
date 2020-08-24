import json

import src.JSONParser as JP


def test_toOntologyHierarchy():
    with open('tests/mocks/Ontologies.json') as mockOntologies:
        mockJSON = json.load(mockOntologies)
        data = JP.toOntologyHierarchy(mockJSON)
        assert data is not None and not data.empty
