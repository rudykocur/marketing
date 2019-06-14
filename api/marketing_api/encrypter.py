from cryptography.fernet import Fernet


class Encrypter(object):
    """
    This is really simple mock of real secure encrypter.

    The point of this is not to store plaintext passwords in database. Obfuscation is better than plaintext password.

    Storing key in code is not a good solution, but this is just proof-of-concept :^)
    """
    def __init__(self):
        self.key = b'XvoyY4R3s0pOrjch-YhkMll6Gx1X6YG2akvJZ8RoK0M='
        self.fernet = Fernet(self.key)

    def encrypt(self, value: str) -> str:
        return self.fernet.encrypt(value.encode('utf8')).decode('utf8')

    def decrypt(self, value: str) -> str:
        return self.fernet.decrypt(value.encode('utf8')).decode('utf8')
