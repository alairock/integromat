from integromat_wrapper.integromat import Modules, MTYPE_ACTION


def test_modules(api_key, imtapp):
    name, version = imtapp
    imtmodule = Modules(api_key, name, version)

    # Create a module
    created_module = imtmodule.create('testingModuleCreate', 'Testing Module', 'Testing Module', MTYPE_ACTION)
    module_name = created_module.get('name')
    assert module_name == 'testingModuleCreate'

    # list modules
    modules = imtmodule.list()
    assert len(modules) > 0

    # update modules
    ## Add communications update
    data = [{'type': 'communication'}]
    r = imtmodule.update_communications(module_name, data)
    assert r == {}

    data = [{'type': 'parameters'}]
    r = imtmodule.update_parameters(module_name, data)
    assert r == {}

    data = [{'type': 'mappable'}]
    r = imtmodule.update_mappable_parameters(module_name, data)
    assert r == {}

    data = [{'type': 'interface'}]
    r = imtmodule.update_interface(module_name, data)
    assert r == {}

    data = {'type': 'samples'}
    r = imtmodule.update_samples(module_name, data)
    assert r == {}

    data = [{'type': 'scope'}]
    r = imtmodule.update_scope(module_name, data)
    assert r == {}
