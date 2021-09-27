import pytest
from integromat_wrapper.integromat import Apps, AioApps


def test_get_apps(api_key):
    # test connection to integromat api
    imt_apps = Apps(api_key)

    # create a new app
    created_app = imt_apps.create_app('test-app-1-hw', 'Test App 1')
    newapp_name = created_app.get('name')
    newapp_version = created_app.get('version')
    assert newapp_version is not None

    # delete the above created app (cleanup)
    deleted_app = imt_apps.delete_app(newapp_name, newapp_version)
    assert deleted_app == {}

    # test list apps
    response = imt_apps.list_apps()
    assert len(response) > 0


@pytest.mark.asyncio
async def test_async_get_apps(api_key):
    imt_apps = AioApps(api_key)
    response = await imt_apps.list_apps()
    assert len(response) > 0


def test_get_imtapp_fixture(imtapp):
    name, version = imtapp
    assert 'test-app-1' in name
    assert version == 1
