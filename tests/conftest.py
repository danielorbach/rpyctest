"""
ROOT CONFTEST
"""

pytest_plugins = "pytester", "rpyctest.plugin"


def pytest_collect_targets(session):
    """
    Called during the collection stage to gather preliminary knowledge of accessible remote-targets.
    :return: a list of rpyc.classic connections
    """
    # return 'remote', 'host'
    return 'conn1', 'conn2', 'conn3'


def pytest_target_factory(request, name, target):
    import rpyc
    return rpyc.classic.connect('localhost', 18812)

