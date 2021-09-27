from integromat_wrapper.integromat import General


def test_general(api_key, imtapp):
    name, version = imtapp
    imtgeneral = General(api_key, name, version)

    # Create a general
    data = {'type': 'base'}
    r = imtgeneral.update_base(data)
    assert r == {}

    data = [{'type': 'common'}]
    r = imtgeneral.update_common(data)
    assert r == {}

    data = [{'type': 'groups'}]
    r = imtgeneral.update_groups(data)
    assert r == {}

    data = '# Readme\n## Test readme\n\nThis is a readme'
    r = imtgeneral.update_readme(data)
    assert r == {}
