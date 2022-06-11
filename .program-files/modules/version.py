from time import time
from modules.config_manager import ConfigManager


class VersionManager:
    def __init__(self, daysInCache: float) -> None:
        self.configManager = ConfigManager()
        self.configKey = 'VERSION'
        self.daysInCache = daysInCache if daysInCache > 0 else 1

    # readVersion is not used...
    def readVersion(self) -> str:
        return self.configManager.read(self.configKey) or ''

    def writeVersion(self, version: str) -> None:
        return self.configManager.write(self.configKey, version)

    def shouldResetCache(self) -> bool:
        accessTime = self.configManager.accessTime(self.configKey)
        if (accessTime == None):
            return True
        milliDiff = time() - accessTime
        dayDiff = milliDiff / 86400000
        return dayDiff >= self.daysInCache
