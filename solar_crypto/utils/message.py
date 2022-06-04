import json

from solar_crypto.identity.private_key import PrivateKey
from solar_crypto.utils.crypto import sign_schnorr, verify_schnorr


class Message(object):
    def __init__(self, **kwargs):
        for k in kwargs.keys():
            if k in ["message", "signature", "publickey", "publicKey"]:
                self.__setattr__(k, kwargs[k])
            else:
                raise TypeError("Invalid keyword argument %s" % k)

    @classmethod
    def sign(cls, message, passphrase):
        """Signs a message

        Args:
            message (str/bytes): a message you wish to sign
            passphrase (str): passphrase you wish to use to sign the message

        Returns:
            Message: returns a message object
        """
        message_bytes = message if isinstance(message, bytes) else message.encode()
        private_key = PrivateKey.from_passphrase(passphrase)
        signature = sign_schnorr(message_bytes, private_key)
        return cls(message=message, signature=signature, publicKey=private_key.public_key)

    def verify(self):
        """Verify the Message object

        Returns:
            bool: returns a boolean - true if verified, false if not
        """
        message = self.message if isinstance(self.message, bytes) else self.message.encode()
        public_key = self.publickey if hasattr(self, "publickey") else self.publicKey
        is_verified = verify_schnorr(message, public_key, self.signature)
        return is_verified

    def to_dict(self):
        """Return a dictionary of the message

        Returns:
            dict: dictionary consiting of public_key, signature and message
        """
        data = {
            ("publicKey" if hasattr(self, "publicKey") else "publickey"): (
                self.publicKey if hasattr(self, "publicKey") else self.publickey
            ),
            "signature": self.signature,
            "message": self.message,
        }
        return data

    def to_json(self):
        """Returns a json string of the the message

        Returns:
            str: json string consisting of public_key, signature and message
        """
        data = self.to_dict()
        return json.dumps(data)
