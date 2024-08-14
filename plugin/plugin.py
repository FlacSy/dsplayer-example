from typing import Dict, Any
from dsplayer.plugin_system.plugin_interface import PluginInterface
from dsplayer.engines_system.engine_interface import EngineInterface
from dsplayer.utils.debug import Debuger


class Plugin(PluginInterface):
    def __init__(self):
        self.name = "Plugin"
        self.url_patterns = [
        ]
        self.settings = {}
        self.debug_mode = False
        self.debug_print = Debuger(self.debug_mode).debug_print
        self.debug_print("Plugin initialized")

    def debug(self):
        self.debug_mode = True

    def on_plugin_load(self) -> None:
        self.debug_print("Plugin loaded")

    def on_plugin_unload(self) -> None:
        self.debug_print("Plugin unloaded")

    def get_url_patterns(self) -> list:
        self.debug_print(f"URL patterns: {self.url_patterns}")
        return self.url_patterns

    def get_plugin_name(self) -> str:
        self.debug_print(f"Plugin name: {self.name}")
        return self.name

    def get_settings(self) -> Dict[str, Any]:
        print(f"Current settings: {self.settings}")
        return self.settings

    def update_settings(self, settings: Dict[str, Any]) -> None:
        print(f"Updating settings: {settings}")
        self.settings.update(settings)

    async def search(self, data: str, engine: EngineInterface) -> Dict[str, Any]:
        print(f"Searching with data: {data}")
        # Ваша логика для плагина 
