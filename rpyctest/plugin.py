"""
# PyTest Plugin Hooks

[see more](https://docs.pytest.org/en/latest/reference.html#hooks)
[flowchart](https://github.com/pytest-dev/pytest/issues/3261)

# TODO
custom markers: http://doc.pytest.org/en/latest/example/markers.html
lazy fixtures: https://github.com/TvoroG/pytest-lazy-fixture/blob/master/pytest_lazyfixture.py
"""
import itertools

from .fixtures import RpycManager


def pytest_addhooks(pluginmanager):
    """https://docs.pytest.org/en/latest/reference.html#_pytest.hookspec.pytest_addhooks"""
    from . import newhooks
    pluginmanager.add_hookspecs(newhooks)


def pytest_configure(config):
    """https://docs.pytest.org/en/latest/reference.html#_pytest.hookspec.pytest_configure"""
    pass


def pytest_sessionstart(session):
    """https://docs.pytest.org/en/latest/reference.html#_pytest.hookspec.pytest_sessionstart"""
    targets = itertools.chain(*session.config.hook.pytest_collect_targets(session=session))
    session.config.pluginmanager.register(RpycManager(session, targets))


def pytest_collection(session):
    """https://docs.pytest.org/en/latest/reference.html#_pytest.hookspec.pytest_collection"""
    pass


def pytest_generate_tests(metafunc):
    """https://docs.pytest.org/en/latest/reference.html#_pytest.hookspec.pytest_generate_tests"""
    pass
