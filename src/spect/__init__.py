import sys
from .spect import Spect


class SpectCaller(sys.modules[__name__].__class__):
    def __call__(self, obj):  # module callable
        return Spect(obj)


sys.modules[__name__].__class__ = SpectCaller
