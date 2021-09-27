from integromat_wrapper.integromat import Functions


def test_functions(api_key, imtapp):
    name, version = imtapp
    imtfunctions = Functions(api_key, name, version)

    # Create a function
    created_function = imtfunctions.create('testingFunctions')
    function_name = created_function.get('name')
    assert function_name == 'testingFunctions'

    # list functions
    functions = imtfunctions.list()
    assert len(functions) > 0

    # update functions
    data = '''function testingFunctions(c) {\nlet a = 10;\nlet b = 20;\nreturn a+b+c;\n}\n'''
    r = imtfunctions.update_code(function_name, data)
    assert r == {}

    # update tests
    data = '''function test_testingFunctions(c) {\nlet a = 10;\nlet b = 20;\nreturn a+b+c;\n}\n'''
    r = imtfunctions.update_test(function_name, data)
    assert r == {}
