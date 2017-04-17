import pytest

from fixture.application import Application
import json
import os.path

fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target

    browser = request.config.getoption("--browser")
    config = request.config.getoption("--target")

    if target is None:
        full_config_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), config)
        with open(full_config_name) as config_file:
            target = json.load(config_file)
    if (fixture is None) or (not fixture.is_valid()):
        fixture = Application(browser = browser, base_url = target["baseUrl"])
    fixture.session.ensure_login(user=target["user"], password=target["password"])

    return fixture

@pytest.fixture(scope = 'session', autouse = True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action ="store", default = "firefox")
    parser.addoption("--target", action ="store", default = "target.json")

