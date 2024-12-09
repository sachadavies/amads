import pkgutil
import importlib
import os
from amads.core import export_registry

package_dir = os.path.dirname(__file__)
for _, module_name, _ in pkgutil.walk_packages([package_dir], prefix='amads.'):
    importlib.import_module(module_name)

# Add exported objects to the all.py namespace with optional export names
for export_name, obj in export_registry:
    globals()[export_name] = obj


