from integromat_wrapper.integromat import Connections


def test_connections(api_key, imtapp):
    name, version = imtapp
    imtconnections = Connections(api_key, name)

    # Create a connections
    created_connections = imtconnections.create('imtconnect_test')
    connections_name = created_connections.get('name')
    connections_label = created_connections.get('label')
    assert connections_label == 'imtconnect_test'

    # list connectionss
    connectionss = imtconnections.list()
    assert len(connectionss) > 0

    data = [{'type': 'communication'}]
    r = imtconnections.update_communications(connections_name, data)
    assert r == {}

    data = [{'type': 'common'}]
    r = imtconnections.update_common(connections_name, data)
    assert r == {}

    data = {'type': 'scopes'}
    r = imtconnections.update_scopes(connections_name, data)
    assert r == {}

    data = [{'type': 'default_scope'}]
    r = imtconnections.update_default_scope(connections_name, data)
    assert r == {}

    data = [{'type': 'parameters'}]
    r = imtconnections.update_parameters(connections_name, data)
    assert r == {}
