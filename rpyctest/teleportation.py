"""

"""
import functools

import rpyc


class ClassicTeleport(object):
    def __init__(self, conn, globals_=None, def_=True, wrap=False):
        self.conn = conn
        self.globals = globals_
        self.def_ = def_
        self.wrap = wrap

    def __call__(self, func):
        function_netref = rpyc.classic.teleport_function(self.conn, func, self.globals, self.def_)
        if not self.wrap:
            return function_netref

        @functools.wraps(func)
        def remote2local(*args, **kwargs):
            return function_netref(*args, **kwargs)

        return remote2local


def fixture_teleport(conn, globals_=None, def_=True):
    return ClassicTeleport(conn, globals_, def_, wrap=True)
