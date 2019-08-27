"""

"""

import rpyc
import pytest

import rpyctest

#
# @rpyctest.remote_fixture(remote='remote_id1')
# def remote_fixture_func(remote_id1):
#     pass


conn1 = rpyc.connect('localhost', 18812)
conn2 = rpyc.connect('localhost', 18812)
conn3 = rpyc.connect('localhost', 18812)


def remote_fixture(**kwargs):
    parametrize = pytest.mark.parametrize('conn', [conn1, conn2, conn3])
    return pytest.fixture(**kwargs)(parametrize)


# remote fixture
@remote_fixture()
def os_module(conn):
    return conn.modules.os
# --------------


# remote fixture
@pytest.fixture()
@pytest.mark.parametrize('conn', [conn1, conn2, conn3])
def os_module(conn):
    return conn.modules.os
# --------------


@pytest.fixture()
def remote_getcwd(os_module):
    return os_module.getcwd()


def test_remote_fixture(remote_getcwd):
    assert remote_getcwd
