import amads.all
from ..core.export import export

@export
def my_exported_function():
    """
    Brief description of my_exported_function.

    Detailed explanation of what my_exported_function does.
    """
    pass

@export("custom_exported_name")
def another_function():
    """
    Brief description of another_function.

    Detailed explanation of what another_function does.
    """
    pass

amads.all.find_root_parncutt_1988()

@export
class MyExportedClass:
    """
    Brief description of MyExportedClass.

    Detailed explanation of what MyExportedClass does.
    """
    def __init__(self):
        pass

@export(name="test_class2")
class A:
    pass

@export("test_class")
class AnotherExportedClass:
    """
    Brief description of AnotherExportedClass.

    Detailed explanation of what AnotherExportedClass does.
    """
    def __init__(self):
        pass

# Exporting a constant
export("EXPORTED_CONSTANT", 42)