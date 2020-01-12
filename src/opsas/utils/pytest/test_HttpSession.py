from ..HttpSession import HttpSession
import pytest
import logging


@pytest.fixture(scope='class')
def session(pytestLogger, pytestConfiger):
    s = HttpSession(logger=pytestLogger, endpoint="https://jsonplaceholder.typicode.com")
    yield s
    s.session.close()


# @pytest.fixture()
def logger():
    l = logging.getLogger()
    l.error('error')
    print(l.level)
    return l


class TestHttpSession:
    def test_request_conn_get(self, session):
        conn = session.request_conn('/')
        assert conn.status_code == 200

    def test_read_json(self, session):
        user_data = session.read_json('/users/1')
        assert user_data['id'] == 1

    def test_request_conn_post(self, session):
        user_data = {"id": 13, 'name': "Test13"}
        conn = session.request_conn("/users/", 'post', data=user_data)
        print(conn.json())