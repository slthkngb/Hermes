import importlib
import os
from typing import Dict, Type

class PluginInterface:
    # A base class or interface all plugins must implement
    def initialize(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

class PluginManager:
    def __init__(self):
        self.plugins: Dict[str, PluginInterface] = {}

    def register_plugin(self, name: str, plugin: PluginInterface):
        self.plugins[name] = plugin

    def load_plugins_from_folder(self, folder_path: str):
        # Dynamically discover and import .py files in the folder
        for file in os.listdir(folder_path):
            if file.endswith(".py") and not file.startswith("__"):
                module_name = file[:-3]
                module = importlib.import_module(f"{folder_path}.{module_name}")
                # The module should have a register function or something similar
                if hasattr(module, "register"):
                    module.register(self)

    def get_plugin(self, name: str):
        return self.plugins.get(name)

    def list_plugins(self):
        return list(self.plugins.keys())
