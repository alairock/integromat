import pytest
from integromat_wrapper.integromat import IMTBasic, AioIMTBasic


def test_connection(api_key):
    # ensure api_key exists, you must add the environment variable to run these tests
    assert api_key is not None

    # test connection to integromat api
    imt_basic = IMTBasic(api_key)
    assert imt_basic.api_key is not None

    response = imt_basic.whoami()
    assert response.get('email') is not None


@pytest.mark.asyncio
async def test_async_connection(api_key):
    # ensure api_key exists, you must add the environment variable to run these tests
    assert api_key is not None

    # test connection to integromat api
    imt_basic = AioIMTBasic(api_key)
    assert imt_basic.api_key is not None

    response = await imt_basic.whoami()
    assert response.get('email') is not None

