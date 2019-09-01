"""
define custom hooks
"""


def pytest_collect_targets(session):
    """
    Called during the collection stage to gather preliminary knowledge of accessible remote-targets.
    :return: a list of rpyc.classic connections
    """
    pass


def pytest_target_factory(config, target):
    """
    """
    pass
