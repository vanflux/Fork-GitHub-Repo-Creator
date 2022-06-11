import base64
from modules.config_manager import ConfigManager


class TokenManager:
    def __init__(self) -> None:
        self.configManager = ConfigManager()
        self.configKey = 'TOKEN'

    def readToken(self) -> str:
        base64Token = self.configManager.read(self.configKey) or ''
        base64Bytes = base64Token.encode("ascii")
        tokenBytes = base64.b64decode(base64Bytes)
        return tokenBytes.decode("ascii")

    def writeToken(self, accessToken: str) -> None:
        tokenBytes = accessToken.encode("ascii")
        base64Bytes = base64.b64encode(tokenBytes)
        base64Token = base64Bytes.decode("ascii")
        self.configManager.write(self.configKey, base64Token)
