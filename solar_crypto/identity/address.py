import hashlib
from binascii import unhexlify
from typing import Optional

from base58 import b58decode_check, b58encode_check
from binary.unsigned_integer.writer import write_bit8
from Crypto.Hash import RIPEMD160

from solar_crypto.configuration.network import get_network
from solar_crypto.identity.private_key import PrivateKey


def address_from_public_key(public_key: str, network_version: Optional[int] = None) -> str:
    """Get an address from a public key

    Args:
        public_key (str):
        network_version (int, optional):

    Returns:
        str: address string
    """
    if not network_version:
        network = get_network()
        network_version = network["version"]

    ripemd160 = RIPEMD160.new()
    ripemd160.update(unhexlify(public_key))
    seed = write_bit8(network_version) + ripemd160.digest()
    return b58encode_check(seed).decode()


def address_from_private_key(private_key: str, network_version: Optional[int] = None) -> str:
    """Get an address from private key

    Args:
        private_key (string)
        network_version (int, optional)

    Returns:
        str: address string
    """
    if not network_version:
        network = get_network()
        network_version = network["version"]

    pvt_key = PrivateKey.from_hex(private_key)
    ripemd160 = RIPEMD160.new()
    ripemd160.update(unhexlify(pvt_key.public_key))
    seed = write_bit8(network_version) + ripemd160.digest()
    return b58encode_check(seed).decode()


def address_from_passphrase(passphrase: str, network_version: Optional[int] = None) -> str:
    """Get an address from passphrase

    Args:
        passphrase (str):
        network_version (int, optional):

    Returns:
        string: address
    """
    if not network_version:
        network = get_network()
        network_version = network["version"]

    private_key = hashlib.sha256(passphrase.encode()).hexdigest()
    address = address_from_private_key(private_key, network_version)
    return address


def validate_address(address: str, network_version: Optional[int] = None) -> bool:
    """Validate a given address

    Args:
        address (str): address you wish to validate
        network_version (None, optional): custom network version, if none provided fallback to the default network version

    Returns:
        bool
    """
    if not network_version:
        network = get_network()
        network_version = network["version"]

    return network_version == b58decode_check(address)[0]
