# __init__.py for package musmart

# The goal here is to allow algorithms to appear as immediate members
# of the musmart package, e.g. you can write musmart.durdist1 instead
# of having to write musmart.algorithm.durdist1, which is implied by
# the hierarchy of the source tree.
#
# We could accomplish this by writing something like
#    from .algorithm import durdist1
# but this would immediately import durdist1 and *every module in the
# entire package* when you import musmart. Since we expect musmart to
# contain many possibly large algorithms and possibly have dependencies
# on large packages, this is not what we want.
#
# The solution here is to use lazy imports. Thanks to Copilot for
# providing the basic solution.

from .core.basics import *
from .core.timemap import *
from .music import example
import sys
import importlib

from importlib import resources 
import os

# this line is needed for python 3.10 and above
from importlib import abc

class LazyLoader(importlib.abc.Loader):
    def __init__(self, module_name):
        self.module_name = module_name
        self.module = None

    def load_module(self, fullname):
        if self.module is None:
            self.module = importlib.import_module(self.module_name)
        sys.modules[fullname] = self.module
        return self.module

class LazyFinder(importlib.abc.MetaPathFinder):
    def __init__(self, lazy_modules):
        self.lazy_modules = lazy_modules

    def find_spec(self, fullname, path, target=None):
        if fullname in self.lazy_modules:
            return importlib.machinery.ModuleSpec(fullname,
                           LazyLoader(self.lazy_modules[fullname]))
        return None

# List of lazy-loaded modules
lazy_modules = {
    # 'musmart.durdist1': 'musmart.algorithm.durdist1',
    # Add more lazy-loaded modules here
}

def make_lazy_modules(subdirectory):

    def find_python_files(package, subdirectory):
        python_files = []
        # alternative to resources.path() for python 3.11
        with resources.as_file(resources.files(package).joinpath(subdirectory)) as subdir:
        # with resources.path(package, subdirectory) as subdir:
            for root, dirs, files in os.walk(subdir):
                for file in files:
                    if file.endswith('.py'):
                        python_files.append(os.path.join(root, file))
        return python_files

    files = find_python_files(__name__, subdirectory)
    for file in files:
        basename = os.path.splitext(os.path.basename(file))[0]
        lazy_modules[__name__ + "." + basename] = \
                __name__ + "." + subdirectory + "." + basename
        print("Defined", basename, "as", __name__ + "." + basename,
              "in lazy_modules")

# Make all .py files in these subdirectories lazily loaded modules:
make_lazy_modules("algorithm")
make_lazy_modules("io")
make_lazy_modules("music")
make_lazy_modules("resources")

if not any(isinstance(finder, LazyFinder) for finder in sys.meta_path):
    sys.meta_path.insert(0, LazyFinder(lazy_modules))

