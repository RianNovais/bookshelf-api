from http import HTTPStatus

from fastapi.testclient import TestClient

from bookshelf_api.app import app


def test_client():
    test_client = TestClient(app)

    response = test_client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World !'}
