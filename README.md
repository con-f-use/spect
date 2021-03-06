spect
-----

Categorize the `dir()` of a python object.

Essentially filters Python's [dir()](https://docs.python.org/3/library/functions.html#dir) built-in for a given object nicely. Might become a `dir()` pretty printer on steroids at some point and/or a nice helper for quick, interactive debugging / introspecting.


Usage
-----

```python
import spect
import re

respect = spect(re)
print(respect.dunder)  # {'__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__'}
print(respect.private)  # {'_compile', '_locale', '_alphanum_bytes', '_expand', '_alphanum_str', '_MAXCACHE', '_pickle', '_subx', '_pattern_type', '_compile_repl', '_cache'}
print(repsect.const_private) # {'_MAXCACHE'}
```

So far `spect` knows these categories:

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
   or superprivate and contain at least one upper case letter no lower case.

   ```python
   x = spect(...)
   x.const_dunder_superprivate == (x.dunder | x.superprivate) & x.const  # True
   ```

 - _private_alias_: combination of _alias_ and _private_ from above, i.e. equivalent to the set notation:

   ```python
   x.private_alias == x.alias | x.private  # True
   # has all in x.private and x.alias
   ```


Installation
------------

```shell
python -m pip install --user spect
```


ToDo
----

 - Make Python 2 compatible (maybe)
 - Ponder getting magic methods from a list (version dependent!
   hard to future-proof! but no false positives)
   - Think about the use `callable` for Python versions 3.0 to 3.2 where `callable` was deprecated
 - Maybe add a filter for `snake_case`, `camelCase` and `PascalCase`
   (`kebab-case` does not make for valid variable names)
