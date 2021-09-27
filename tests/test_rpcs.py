from integromat_wrapper.integromat import RPCs


def test_rpcs(api_key, imtapp):
    name, version = imtapp
    imtrpcs = RPCs(api_key, name, version)

    # Create a module
    created_rpc = imtrpcs.create('testingrpcs', 'Testing RPC')
    rpc_name = created_rpc.get('name')
    assert rpc_name == 'testingrpcs'

    # list modules
    modules = imtrpcs.list()
    assert len(modules) > 0

    # update modules
    data = [{'type': 'communication'}]
    r = imtrpcs.update_communications(rpc_name, data)
    assert r == {}

    data = [{'type': 'parameters'}]
    r = imtrpcs.update_parameters(rpc_name, data)
    assert r == {}
