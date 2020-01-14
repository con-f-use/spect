spect
-----

Categorize the members of a python object.

Usage
-----

```python
import spect
import re

respect = spect(re)
print(respect.dunder)
print(respect.private)
# output:
# ['all', 'builtins', 'cached', 'doc', 'file', 'loader', 'name', 'package', 'spec', 'version']
# ['MAXCACHE', 'all', 'builtins', 'cached', 'doc', 'file', 'loader', 'name', 'package', 'spec', 'version', 'alphanum_bytes', 'alphanum_str', 'cache', 'compile', 'compile_repl', 'expand', 'locale', 'pattern_type', 'pickle', 'subx']
```

So far it knows:

 - _private_: `_varname`
 - _superprivate_: `__varname`
 - _alias_: `varname_`
 - _dunder_: `__varname__`
 - _regular_: `varname`

Installation
------------

```shell
python -m pip install --user spect
```

ToDo
----

 - Make Python 2 compatible
