from os import path
import base64

TOKEN_FILE_PATH = path.abspath(path.join(path.dirname(
    __file__), '../config/TOKEN.txt'))


class TokenManager:
    def __init__(self) -> None:
        pass

    def readToken(self) -> str:
        with open(TOKEN_FILE_PATH, 'r') as tokenFile:
            base64Token = tokenFile.readline()
            base64Bytes = base64Token.encode("ascii")
            tokenBytes = base64.b64decode(base64Bytes)
            return tokenBytes.decode("ascii")

    def writeToken(self, accessToken: str) -> None:
        with open(TOKEN_FILE_PATH, 'w') as tokenFile:
            tokenBytes = accessToken.encode("ascii")
            base64Bytes = base64.b64encode(tokenBytes)
            base64Token = base64Bytes.decode("ascii")
            tokenFile.write(base64Token)
