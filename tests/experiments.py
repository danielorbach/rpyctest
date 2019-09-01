"""
WIP: development experiments
"""
import pytest
import rpyc


conn1 = rpyc.classic.connect('localhost', 18812)
conn2 = rpyc.classic.connect('localhost', 18812)
conn3 = rpyc.classic.connect('localhost', 18812)


# remote fixture
@pytest.fixture()
def os_module():
    import os
    return os
# --------------


# remote fixture
# @pytest.fixture()
# @pytest.mark.parametrize('conn', [conn1, conn2, conn3])
# def os_module(conn):
#     return conn.modules.os
# --------------


def test_example(os_module):
    import os
    print(os.__file__)
    assert os_module
    print(os_module.__file__)
    assert os.__file__ != os_module.__file__


def test(remote):
    print(remote)
