spect
-----

Categorize the items of a python object.

Essentially filters Python's [dir()](https://docs.python.org/3/library/functions.html#dir) built-in for a given object nicely. Might become a `dir()` pretty printer on steroids at some point. Can be nice for quick interactive debugging / introspecting.


Usage
-----

```python
import spect
import re

respect = spect(re)
print(respect.dunder)  # {'__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__'}
print(respect.private)  # {'_compile', '_locale', '_alphanum_bytes', '_expand', '_alphanum_str', '_MAXCACHE', '_pickle', '_subx', '_pattern_type', '_compile_repl', '_cache'}
```

So far it knows these categories:

- _regular_: `varname`

 - _alias_: `varname_`
 - _dunder_: `__varname__`
 - _private_: `_varname`
 - _superprivate_: `__varname`
 - _general_: an alias for _regular_, so `varname` as well
 - _magic_: double underscore delimitered (dunder) and callable (e.g. `__init__`)
 - _const_: any of the above as long as it has letters and all of them are uppercase (e.g. `_MAXCACHE`)

The categories can be combined and are sets (as are their combinations):

 - _const_dunder_superprivate_: all that are either double underscore delimitered
   or superprivate and contain no lower case letters. That is equivalent to:

   ```python
   x = spect(...)
   (x.dunder | x.superprivate) & x.const == x.const_dunder_superprivate   # True
   ```

 - _private_alias_: alias or private, i.e. `x.alias | x.private`


Installation
------------

```shell
python -m pip install --user spect
```


ToDo
----

 - Make Python 2 compatible (maybe)
 - Convert basic tests to pytest ones
 - Auto-build, test and upload to pypi on commit
 - Ponder getting magic methods from a list (version dependent! hard to future prove! but no false positives)
 - Think about `callable` and Python 3.0 to 3.2 where it was deprecated
