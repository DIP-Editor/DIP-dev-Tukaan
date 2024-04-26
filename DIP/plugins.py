from importlib.machinery import ModuleSpec
from importlib.util import module_from_spec, spec_from_file_location
from types import ModuleType


def get_extension_info(
    filename: str,
) -> tuple[ModuleType, str, str] | None:
    """Get the info of an extension."""

    # Load the extension and call the Extension class
    try:
        spec: ModuleSpec | None = spec_from_file_location(
            name="Extension", location=filename
        )
    except Exception as e:
        print(e)
        return

    if spec is None:
        return

    extension = module_from_spec(spec)
    loader = spec.loader
    if loader is None:
        return
    loader.exec_module(extension)
    version: str = getattr(extension.Extension, "version", "1.0.0")
    author: str = getattr(extension.Extension, "author", "Unknown")

    return (extension, version, author)
