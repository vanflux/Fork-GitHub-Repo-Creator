from os import path
from pathlib import Path
from typing import Optional


class ConfigManager:
    def __init__(self) -> None:
        self.configPath = path.abspath(
            path.join(path.dirname(__file__), '../config'))

    def _getItemPath(self, key) -> str:
        return path.abspath(path.join(self.configPath, key))

    def exists(self, key) -> bool:
        return path.exists(self._getItemPath(key))

    def read(self, key) -> Optional[str]:
        if (not self.exists(key)):
            return None
        with open(self._getItemPath(key), 'r') as file:
            return file.readline()

    def write(self, key, value: str) -> None:
        if (not self.exists(key)):
            Path(self._getItemPath(key)).parent.mkdir(exist_ok=True, parents=True)
        with open(self._getItemPath(key), 'w') as file:
            file.write(value)
    
    def accessTime(self, key) -> Optional[float]:
        if (not self.exists(key)):
            return None
        return path.getatime(self._getItemPath(key))
