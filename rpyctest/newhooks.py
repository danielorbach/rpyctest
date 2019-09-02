"""
define custom hooks
"""
import pytest


# noinspection PyUnusedLocal
def pytest_collect_targets(session):
    """
    Called during the collection stage to gather preliminary knowledge of accessible remote-targets.
    The objects returned are stored in a mapping of actual remote-connection objects
    (acquired from `pytest_target_factory`).
    Each object's 'name' attribute will be used as the key for this mapping. In case there is no such attribute,
    the `__str__` method will be used.
    :return: an iterable of immutable objects
    """
    pass


# noinspection PyUnusedLocal
@pytest.hookspec(firstresult=True)
def pytest_target_factory(request, name, target):
    """
    Associates a connection object with a target.
    :param request: fixture's request object
    :param target: acquired from `pytest_collect_targets`
    :param name: fixture name (as exposed to test items)
    :return: an `rpyc.classic` connection
    """
    pass
