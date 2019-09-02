import pytest
import rpyc


def pytest_collect_targets(session):
    class FixtureFactory:
        def __init__(self, name):
            self.name = name

        def fixture(self):
            return object()

    yield FixtureFactory('conn4')
    yield FixtureFactory('conn5')
    yield type('AnonymousFixture', (object,), {'name': 'conn6', 'fixture': lambda: object()})


@pytest.fixture()
def conn4():
    return rpyc.classic.connect('localhost', 18812)

#
# def pytest_target_factory(request, name, target):
#     assert name not in ['conn4', 'conn5', 'conn6']
#     return globals()[name]
