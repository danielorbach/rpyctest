"""
WIP: development experiments
"""
import pytest
import rpyc


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


def test_multi_arg(conn1, conn2, conn3):
    assert isinstance(conn1, rpyc.core.protocol.Connection)
    print(conn1)
    assert isinstance(conn2, rpyc.core.protocol.Connection)
    print(conn2)
    assert isinstance(conn3, rpyc.core.protocol.Connection)
    print(conn3)


@pytest.fixture(name='conn', params=['conn1', 'conn2', 'conn3'])
def single_arg_conn(request):
    return request.getfixturevalue(request.param)


def test_single_arg(conn):
    assert isinstance(conn, rpyc.core.protocol.Connection)
    print(conn)
