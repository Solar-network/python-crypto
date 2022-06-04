import hashlib
from binascii import unhexlify

from btclib.ecc import ssa

from solar_crypto.identity.private_key import PrivateKey
from solar_crypto.schnorr import schnorr


def sign_schnorr(msg: bytes, private_key: PrivateKey, nonce: int = None) -> str:
    """Signs a message using Schnorr BIP340

    Args:
        msg (bytes): a message you wish to sign
        private_key (PrivateKey): private key object
        nonce (int): deterministic nonce

    Returns:
        str: returnes a hex string of a signature
    """
    signature = ssa.sign(msg, private_key.to_hex(), nonce)
    return signature.serialize().hex()


def sign_schnorr_legacy(msg: bytes, private_key: PrivateKey) -> str:
    """Signs a message using Legacy Schnorr

    Args:
        msg (bytes): a message you wish to sign
        private_key (PrivateKey): private key object
        nonce (int): deterministic nonce

    Returns:
        str: returnes a hex string of a signature
    """
    msg = hashlib.sha256(msg).digest()
    secret = unhexlify(private_key.to_hex())
    signature = schnorr.bcrypto410_sign(msg, secret).hex()
    return signature


def verify_schnorr(msg: bytes, public_key: str, signature: str) -> bool:
    """Verifies a message using Schnorr BIP340

    Args:
        msg (bytes): a message you wish to sign
        public_key (str)
        signature (str)

    Returns:
        bool
    """
    return ssa.verify(msg, public_key, signature)


def verify_schnorr_legacy(msg: bytes, public_key: str, signature: str) -> bool:
    """Verifies a message using Legacy Schnorr

    Args:
        msg (bytes): a message you wish to sign
        public_key (str)
        signature (str)

    Returns:
        bool
    """
    return schnorr.b410_schnorr_verify(msg, public_key, signature)
