import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import ModuleType


def load_module_from_path(path: Path, name: str = "module") -> ModuleType | None:
    spec = spec_from_file_location(name, path)
    if spec is not None:
        module = module_from_spec(spec)
        sys.modules["module.name"] = module
        if spec.loader:
            spec.loader.exec_module(module)
            return module
