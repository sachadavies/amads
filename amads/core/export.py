export_registry = []

def export(obj=None, name=None):
    """
    Decorator or function to mark functions, classes, or constants for export in all.py.

    Usage as a decorator:
        @export
        def func():
            ...

        @export("custom_name")
        class MyClass:
            ...

    Usage as a function for exporting constants:
        export("CONSTANT_NAME", constant_value)

    Parameters
    ----------
    obj : callable, optional
        The function or class to be exported when used as a decorator.
    name : str, optional
        The name under which to export the object. If not provided when used as a decorator,
        the object's original name is used.

    Returns
    -------
    callable or None
        Returns the decorator function when used as a decorator.
        Returns None when used as a function to export constants.
    """
    if callable(obj):
        # Used as @export without arguments
        export_name = name or obj.__name__
        export_registry.append((export_name, obj))
        return obj
    elif isinstance(obj, str) and name is not None:
        # Used as export(name, value) for constants
        export_registry.append((obj, name))
    elif isinstance(obj, str) and name is None:
        # Used as @export("custom_name") decorator
        def decorator(obj_to_export):
            export_name = obj or obj_to_export.__name__
            export_registry.append((export_name, obj_to_export))
            return obj_to_export
        return decorator
    else:
        raise ValueError("Invalid usage of export. Use as a decorator or export(name, value).")