import src.CSVParser as CSVP


def test_to_instance_count():
    with open('tests/mocks/AllInstances', 'rb') as mockCSV:
        csv_data = mockCSV.read()
        table = CSVP.to_all_instances_count(csv_data)
        assert table is not None and not table.empty


def test_parse_query_response():
    with open('tests/mocks/InstancesCount', 'rb') as mockCSV:
        csv_data = mockCSV.read()
        table = CSVP.parse_query_response(csv_data)
        assert table is not None and not table.empty
