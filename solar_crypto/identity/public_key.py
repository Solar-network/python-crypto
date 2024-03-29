from __future__ import annotations

from binascii import hexlify, unhexlify

from coincurve import PublicKey as PubKey

from solar_crypto.identity.private_key import PrivateKey


class PublicKey(object):
    def __init__(self, public_key: str):
        public_key = unhexlify(public_key.encode())
        self.public_key = PubKey(public_key)

    def to_hex(self) -> str:
        """Returna hex string of a PublicKey object

        Returns:
            str: _description_
        """
        return hexlify(self.public_key.format()).decode()

    @classmethod
    def from_passphrase(cls, passphrase: str) -> str:
        """Return a public key hex string from a given passphrase

        Args:
            passphrase (str)

        Returns:
            str: public key hex string
        """
        private_key = PrivateKey.from_passphrase(passphrase)
        return private_key.public_key

    @classmethod
    def from_hex(cls, public_key: str) -> PublicKey:
        """Create a PublicKey object from a given hex public key string

        Args:
            public_key (str): public key string

        Returns:
            PublicKey
        """
        return cls(public_key)
