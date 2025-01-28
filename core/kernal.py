# kernel.py
from .config import load_config, HermesConfig
from .logging import get_logger
from .plugin_manager import PluginManager
from .environment import setup_device

class HermesCore:
    def __init__(self, config_path: str = None):
        # 1. Load config
        self.config: HermesConfig = load_config(config_path)
        # 2. Set up logger
        self.logger = get_logger("HermesCore", level=self.config.log_level)
        # 3. Device setup
        self.device = setup_device()
        # 4. Plugin manager
        self.plugin_manager = PluginManager()
        self.logger.info("HermesCore initialized.")

    def load_plugins(self, plugin_path: str = "hermes/plugins"):
        self.plugin_manager.load_plugins_from_folder(plugin_path)
        self.logger.info(f"Loaded plugins: {self.plugin_manager.list_plugins()}")

    def run_plugin(self, plugin_name: str):
        plugin = self.plugin_manager.get_plugin(plugin_name)
        if plugin:
            plugin.initialize()
            plugin.run()
        else:
            self.logger.error(f"Plugin {plugin_name} not found.")
