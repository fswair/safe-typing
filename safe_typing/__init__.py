"""
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
"""

import importlib

class _NotFound:
    """
    A sentinel to indicate that an attribute was not found in the typing namespace.
    """
    pass

NotFound = _NotFound()
"""
A sentinel value to indicate that a type was not found in the typing namespace.
"""

TypingEntity = type | None
"""
A type alias for a type that can either be a valid type from the typing namespace.
"""

SafeEntity = type | _NotFound
"""
A type alias for a type that can either be a valid type from the typing namespace or the NotFound sentinel.
"""

_no_raise: SafeEntity
"""
Import this sentinel to suppress ImportError exceptions when a type is not found.
"""

no_raise: bool = False
"""
Flag variable to suppress ImportError exceptions when a type is not found.
"""

def __getattr__(name: str) -> SafeEntity | TypingEntity | bool:
    """
    Get an attribute from the typing module or typing_extensions module safely.
    """
    if name == "_no_raise":
        global no_raise
        no_raise = True
        return no_raise
    
    try:
        return getattr(importlib.import_module("typing"), name)
    except (ImportError, AttributeError) as exc:
        if no_raise:
            return getattr(
                importlib.import_module("typing_extensions"), name, NotFound
            )
        
        entity = getattr(importlib.import_module("typing_extensions"), name, None)
        if entity is None:
            raise ImportError(
                f"Cannot import name '{name}' from 'typing' or 'typing_extensions'"
            ) from exc
        
        return entity