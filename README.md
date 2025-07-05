Safe Typing is a module that provides a safe way to access types within the typing namespace.
It attempts to import types from the standard `typing` module first, and if not found,
it falls back to the `typing_extensions` module.
If a type is not found in either module, it returns a sentinel value `NotFound`.

Stop writing this:

```python
import sys 

if sys.version_info >= (3, 8):
    from typing import List, Dict, Tuple
else:
    from typing_extensions import List, Dict, Tuple
```

Use this instead:

```python
from typing import List as TypingList, Dict as TypingDict
from safe_typing import _no_raise, List, Dict, FooBar, NotFound

# if you import _no_raise sentinel
# it will not raise an error when a name is not found in the module
# it will return a NotFound sentinel.
# otherwise, it will raise an ImportError
# if the name is not found in both typing and typing_extensions.

assert List is TypingList # True
assert Dict is TypingDict # True
assert FooBar is NotFound  # FooBar does not exist in either typing or typing_extensions

```

You can reach me from contact@tomris.dev for collaborations, bug reports or feature requests.