import re, functools


class Spect(object):
    """Categorize members of an object.

    Examples:
        >>> import re
        >>> repsect = Spect(re)  # The pun is strong in that one
        >>> '__doc__' in respect.dunder
        True
        >>> 'match' in respect.regular
        True
    """

    categorizer = re.compile(
        r"(?P<dunder>__\w+__)|"
        r"(?P<superprivate>__\w+)|"
        r"(?P<private>_\w+)|"
        r"(?P<alias>[a-zA-Z]\w*_)|"
        r"(?P<regular>[a-zA-Z]\w*)"
    )
    categories = list(categorizer.groupindex.keys()) + ["magic", "general"]

    def __init__(self, obj):
        self.obj = obj
        self.dir = set(dir(obj))

        for category in self.categories:
            self.__dict__[category] = []

        for mem in map(self.categorizer.fullmatch, self.dir):
            category = mem.lastgroup
            self.__dict__[category].append(mem[category])

        self.magic = filter(lambda x: callable(getattr(obj, x)), self.dunder)
        self.general = self.regular  # Salute to private & superprivate theme

        for category in self.categories:
            self.__dict__[category] = set(self.__dict__[category])

    def __getattr__(self, attr):
        components = attr.split("_")
        if any(c not in self.categories + ["const"] for c in components):
            raise AttributeError(
                "'{}' has no attribute '{}'".format(self.__class__.__name__, attr)
            )
        const = self.const if "const" in components else self.dir
        components = [self.__dict__[x] for x in components if x != "const"]
        union = functools.reduce(lambda r, l: r | l, components)
        return union & const

    @property
    def const(self):
        upper = lambda s: s == s.upper() and re.sub(r"[0-9_]*", "", s)
        return set(filter(upper, self.dir))


if __name__ == "__main__":
    print('Basic tests...')
    sre = Spect(re)
    assert '__doc__' in sre.dunder
    assert 'match' in sre.regular
    assert '_MAXCACHE' in sre.const_private
    assert sre.const - sre.regular == {'_MAXCACHE'}
    assert '__getattr__' in Spect(sre).magic
    print('Done.')
