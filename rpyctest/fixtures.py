"""

"""
import functools

import pytest


class RpycManager(object):
    """

    """

    def __init__(self, session, targets):
        self._session = session
        for target in targets:
            setattr(self, f'_pytest_{target}', self._generate_fixture(target))

    def _generate_fixture(self, target):
        factory_hook = self._session.config.hook.pytest_target_factory

        @pytest.fixture(scope='session', name=target)
        def target_factory(pytestconfig):
            return factory_hook(config=pytestconfig, target=target)

        return target_factory


def group_filter(scope="function", ids=None, name=None):
    """
    @group_filter('conn')
    def windows_group(rpyc_client):
        return is_windows(rpyc_client)

    def test_func(conn):
        pass
    """
    connections = []

    def fixture_factory(function):
        group = filter(function, connections)

        @pytest.fixture(scope=scope, params=group, ids=ids, name=name)
        @functools.wraps(function)
        def return_connection(request):
            return request.param

        return return_connection

    return fixture_factory
