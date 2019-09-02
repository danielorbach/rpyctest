"""
WIP: development experiments
"""
import pytest
import rpyc


@pytest.fixture()
def conn5():
    return 2


def test_multi_arg(conn3, conn4, conn5, conn6):
    assert isinstance(conn3, rpyc.core.protocol.Connection)
    print(conn3)
    assert isinstance(conn4, rpyc.core.protocol.Connection)
    print(conn4)
    assert conn5 == 2
    print(conn5)
    assert type(conn6) == object
    print(conn6)


@pytest.fixture(name='conn', params=['conn3', 'conn4', 'conn5', 'conn6'])
def single_arg_conn(request):
    return request.getfixturevalue(request.param)


def test_single_arg(conn):
    assert any([isinstance(conn, rpyc.core.protocol.Connection),
                conn == 2, type(conn) == object])
    print(conn)
