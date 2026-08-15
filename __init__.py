"""Bridge module for plugin entry point resolution.

N.E.K.O host's fallback loader expects __init__.py at the plugin root directory.
This bridge re-exports the entry class from the nested plugins/<id>/ directory.
"""
from .plugins.xiyin_pavilion import XiYinPavilionPlugin as XiYinPavilionPlugin

__all__ = ["XiYinPavilionPlugin"]
