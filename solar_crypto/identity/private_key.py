from __future__ import annotations

from binascii import hexlify
from hashlib import sha256

from coincurve import PrivateKey as PvtKey


class PrivateKey(object):
    def __init__(self, private_key: str):
        self.private_key = PvtKey.from_hex(private_key)
        self.public_key = hexlify(self.private_key.public_key.format()).decode()

    def sign(self, message: bytes, nonce: int = None) -> str:
        """Sign a message with this private key object

        Args:
            message (bytes): bytes data you want to sign
            nonce (int): non-deterministic synthetic nonce

        Returns:
            str: signature of the signed message
        """
        from solar_crypto.utils.crypto import sign_schnorr  # circular imports

        signature = sign_schnorr(message, self.private_key, nonce)
        return signature

    def to_hex(self) -> str:
        """Returns a private key in hex format

        Returns:
            str: private key in hex format
        """
        return self.private_key.to_hex()

    @classmethod
    def from_passphrase(cls, passphrase: str) -> PrivateKey:
        """Create PrivateKey object from a given passphrase

        Args:
            passphrase (str):

        Returns:
            PrivateKey: Private key object
        """
        private_key = sha256(passphrase.encode()).hexdigest()
        return cls(private_key)

    @classmethod
    def from_hex(cls, private_key) -> PrivateKey:
        """Create PrivateKey object from a given hex private key

        Args:
            private_key (str):

        Returns:
            PrivateKey: Private key object
        """
        return cls(private_key)
