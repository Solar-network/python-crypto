import hashlib
from typing import Optional

from base58 import b58encode_check
from binary.unsigned_integer.writer import write_bit8

from solar_crypto.configuration.network import get_network


def wif_from_passphrase(passphrase: str, network_wif: Optional[int] = None) -> str:
    """Get wif from passphrase

    Args:
        passphrase (str)
        network_wif (int, optional)

    Returns:
        str: wif string
    """
    if not network_wif:
        network = get_network()
        network_wif = network["wif"]

    private_key = hashlib.sha256(passphrase.encode())
    seed = write_bit8(network_wif) + private_key.digest() + write_bit8(0x01)
    return b58encode_check(seed).decode()
