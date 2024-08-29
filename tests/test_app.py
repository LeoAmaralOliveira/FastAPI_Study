from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_hello_world_must_return_ok_and_hello_world():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Hello World'}  # Assert


def test_hello_world_must_return_ok_and_hello_world_html():
    client = TestClient(app)  # Arrange

    response = client.get('/ola_html')  # Act

    html = """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.text == html  # Assert
