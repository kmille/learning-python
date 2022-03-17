#!/usr/bin/env python3
import sys
import pytest
import requests


"""
References:
- https://docs.pytest.org/en/7.1.x/how-to/index.html
- https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
- https://realpython.com/pytest-python-testing/

useful command line arguments:
- more verbose: -v
- show stdout/prints of test_functions: -s
- run python debugger (pdb) if erros exists: --pdb
- run only tests containing 'network': -k network
- run all tests except ones having 'network' in the name: -k 'not network'
- stop after first failure: -x

"""


@pytest.fixture(autouse=True)
def always_used():
    print("This is always called")


@pytest.fixture
def result():
    return 4


def test_result(result):
    assert result == 4


def test_raise(result):
    with pytest.raises(AttributeError):
        result.dosnotexist()


@pytest.mark.parametrize(('number1', 'number2'), [(1, 3), (2, 2)])
def test_calc_add(result, number1, number2):
    assert result == number1 + number2


@pytest.mark.parametrize(
    ('n', 'expected'), [
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
    ]
)
def test_increment(n, expected):
    assert n + 1 == expected


#### BEGIN faill ####
@pytest.mark.xfail
def test_wrong():
    assert 2 == 2


@pytest.mark.xfail
def test_wrong2():
    assert 1 == 2


def test_wrong3():
    if 1 == 2:
        pytest.xfail("no right")

#### END faill ####



#### BEGIN SKIP ####
@pytest.mark.skip(reason="no way of currently testing this")
def test_not_now():
    assert 1 == 2


@pytest.mark.skipif(sys.version_info > (3, 0), reason="works only with python2")
def test_skip_here():
    assert 1 == 1

#### END SKIP ####


@pytest.fixture
def setup():
    print("SETUP")
    yield
    print("TEARDOWN")


def test_with_cleanup(setup):
    print("TESTING")
    assert 1 == 1


def test_cap_prints(capsys):
    print("OKEEE")
    sys.stderr.write("world\n")
    captured = capsys.readouterr()
    assert captured.err == "world\n"
    assert captured.out == "OKEEE\n"


# pip install requests_mock
def test_mock_request(requests_mock):
    requests_mock.get("https://httpbin.org/anything", json={'ip': '8.8.8.8'},
                      status_code=201, headers={'X-Server': 'php'})
    resp = requests.get("https://httpbin.org/anything")
    assert resp.json()['ip'] == '8.8.8.8'
    assert resp.status_code == 201
    assert 'X-Server' in resp.headers
    assert resp.headers['X-Server'] == 'php'


# custom class to be the mock return value
# will override the requests.Response returned from requests.get
class MockResponse:

    # mock json() method always returns a specific testing dictionary
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


def test_get_json(monkeypatch):

    # Any arguments may be passed and mock_get() will always return our
    # mocked object, which only has the .json() method.
    def mock_get(*args, **kwargs):
        return MockResponse()

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    # app.get_json, which contains requests.get, uses the monkeypatch
    result = requests.get("https://fakeurl").json()
    assert result["mock_key"] == "mock_response"
