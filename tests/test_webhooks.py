from integromat_wrapper.integromat import Webhooks, Connections


def test_webhooks(api_key, imtapp):
    name, version = imtapp
    imtwebhooks = Webhooks(api_key, name)

    # Create a webhook
    created_webhook = imtwebhooks.create('webhook_namez')
    webhook_label = created_webhook.get('label')
    assert webhook_label == 'webhook_namez'
    webhook_name = created_webhook.get('name')

    # list webhooks
    webhooks = imtwebhooks.list()
    assert len(webhooks) > 0

    # update webhooks
    data = [{'type': 'communication'}]
    r = imtwebhooks.update_communications(webhook_name, data)
    assert r == {}

    data = [{'type': 'parameters'}]
    r = imtwebhooks.update_parameters(webhook_name, data)
    assert r == {}

    data = [{'type': 'attach'}]
    r = imtwebhooks.update_attach(webhook_name, data)
    assert r == {}

    data = {'type': 'detach'}
    r = imtwebhooks.update_detach(webhook_name, data)
    assert r == {}

    data = [{'type': 'scope'}]
    r = imtwebhooks.update_scope(webhook_name, data)
    assert r == {}

    # Test attach connection
    imtconnections = Connections(api_key, name)

    # Create a connections
    created_connections = imtconnections.create('imtconnect_test')
    connections_name = created_connections.get('name')

    r = imtwebhooks.add_connection(webhook_name, connections_name)
    assert r == {}
