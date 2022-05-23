import hashlib
from binascii import unhexlify
from btclib.ecc import ssa

from crypto.schnorr import schnorr
from crypto.identity.private_key import PrivateKey


def sign_schnorr(msg: str, private_key: PrivateKey, nonce: int = None) -> str:
    signature = ssa.sign(msg, private_key.to_hex(), nonce)
    return signature.serialize().hex()


def sign_schnorr_legacy(msg: str, private_key: PrivateKey) -> str:
    msg = hashlib.sha256(msg).digest()
    secret = unhexlify(private_key.to_hex())
    signature = schnorr.bcrypto410_sign(msg, secret).hex()
    return signature


def verify_schnorr(msg: str, sender_public_key: str, signature: str) -> bool:
    return ssa.verify(msg, sender_public_key, signature)


def verify_schnorr_legacy(msg: str, sender_public_key: str, signature: str) -> bool:
    return schnorr.b410_schnorr_verify(msg, sender_public_key, signature)
