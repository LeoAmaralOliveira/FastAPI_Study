from http import HTTPStatus


def test_hello_world_must_return_ok_and_hello_world(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'string',
            'email': 'user@example.com',
            'passowrd': 'string',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'string',
        'email': 'user@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'string',
                'email': 'user@example.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'string2',
            'email': 'user2@example.com',
            'passowrd': 'string2',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'string2',
        'email': 'user2@example.com',
        'id': 1,
    }

    response = client.put(
        '/users/1111',
        json={
            'username': 'string2',
            'email': 'user2@example.com',
            'passowrd': 'string2',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_read_user(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'string2',
        'email': 'user2@example.com',
        'id': 1,
    }

    response = client.get('/users/1111')

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}

    response = client.delete('/users/1111')

    assert response.status_code == HTTPStatus.NOT_FOUND
