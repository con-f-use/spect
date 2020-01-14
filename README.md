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
# {'__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__'}
# {'_compile', '_locale', '_alphanum_bytes', '_expand', '_alphanum_str', '_MAXCACHE', '_pickle', '_subx', '_pattern_type', '_compile_repl', '_cache'}
```

So far it knows these categories:

 - _private_: `_varname`
 - _superprivate_: `__varname`
 - _alias_: `varname_`
 - _dunder_: `__varname__`
 - _regular_: `varname`
 - _magic_: double underscore delimetered (dunder) and callable
 - _const_: any of the above as long as it has letters and all of them are uppercase (e.g. `_MAXCACHE`)

The categories can be combined and are sets (as are their combinations):

 - _const_dunder_superprivate_: all that are either double underscore delimetered
   or superprivate and contain no lower case letters. That is equivalent to:

   ```python
   x = spect(...)
   (x.dunder | x.superprivate) & x.const
   ```

 - _prinvate_alias_: alias or private, i.e. `x.alias | x.private`


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
 - Ponder getting magic methods from a list (version dependent!)
 - Think about `callable` and Python 3.0 to 3.2 where it was deprecated
