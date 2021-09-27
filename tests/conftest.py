from pytest import fixture
import os

from integromat_wrapper.integromat import Apps


@fixture
def imtapp(api_key):
    imt_apps = Apps(api_key)
    created_app = imt_apps.create_app('test-app-1-hw', 'Test App 1')
    newapp_name = created_app.get('name')
    newapp_version = created_app.get('version')
    yield newapp_name, newapp_version
    imt_apps.delete_app(newapp_name, newapp_version)


@fixture(scope='session')
def api_key():
    return os.getenv('INTEGROMAT_APIKEY', None)


@fixture(scope='session')
def app():
    return os.getenv('INTEGROMAT_APP', None)


@fixture(scope='session')
def app_version():
    return os.getenv('INTEGROMAT_APP_VERSION', None)





