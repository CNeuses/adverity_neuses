from adverity_neuses.helpers import *

class DebugMeta(type):
    """
    This class provides additional debug information when its subclasses are beeing executed.

    """

    def __new__(meta, name, bases, dct):
        """
        :param name:
        :param bases:
        :param dct:
        :return: final Class Object
        """
        xprint('-----------------------------------')
        xprint("Allocating memory for class", name)
        xprint(meta)
        xprint(bases)
        xprint(dct)
        return super(DebugMeta, meta).__new__(meta, name, bases, dct)

    def __init__(cls, name, bases, dct):
        """
        :param name:
        :param bases:
        :param dct:
        """
        xprint('-----------------------------------')
        xprint("Initializing class", name)
        xprint(cls)
        xprint(bases)
        xprint(dct)
        super(DebugMeta, cls).__init__(name, bases, dct)

    def __call__(cls, *args, **kwds):
        """
        This function is called when a class is called and provides debug info before execution
        :param args:
        :param kwds:
        :return:
        """
        xprint('__call__ of ', str(cls))
        xprint('__call__ *args=', str(args))
        return type.__call__(cls, *args, **kwds)
