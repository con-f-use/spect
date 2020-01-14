import re


class Spect:
    """Categorize members of an object.

    Examples:
        >>> import re
        >>> repsect = Spect(re)
        >>> 'doc' in respect.dunder
        True
        >>> 'match' in respect.regular
        True
    """

    categorizer = re.compile(
        r"__(?P<dunder>\w+)__|"
        r"__(?P<superprivate>\w+)|"
        r"_(?P<private>\w+)|"
        r"(?P<alias>\w+)_|"
        r"(?P<regular>\w+)"
    )

    def __init__(self, obj):
        for category in self.categorizer.groupindex.keys():
            self.__dict__[category] = []

        for mem in map(self.categorizer.fullmatch, dir(obj)):
            category = mem.lastgroup
            self.__dict__[category].append(mem[category])
