"""

"""
import functools

import pytest


class RpycManager(object):
    """

    """

    def __init__(self, session, targets):
        self._session = session
        self._fixtures = {}
        for target in targets:
            name = self._target_name(target)
            fixture = self._generate_fixture(name, target)
            setattr(self, f'_pytest_{name}', fixture)
            self._fixtures[name] = target, fixture

    def _generate_fixture(self, name, target):
        # noinspection PyProtectedMember
        if hasattr(target, 'fixture'):
            return pytest.fixture(scope='session', name=name)(target.fixture)
        factory_hook = self._session.config.hook.pytest_target_factory

        @pytest.fixture(scope='session', name=name)
        def target_factory(request):
            return factory_hook(request=request, name=name, target=target)

        return target_factory

    @staticmethod
    def _target_name(target):
        return target.name if hasattr(target, 'name') else str(target)


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
