# API Reference

This page demonstrates how to integrate Doxygen-generated API documentation with ROCm Docs Core.

## MyNamespace::MyClass

```{doxygenclass} MyNamespace::MyClass
:members:
:protected-members:
:private-members:
```

## Example Usage

Here's how to use the MyClass API:

```cpp
#include <myproject/myclass.h>

MyNamespace::MyClass obj;
if (obj.initialize()) {
    int result = obj.doSomething(42);
    // Process result...
}
```

For more examples, see the [Examples](examples.md) page.
