from datetime import datetime

from solar_crypto.networks.testnet import Testnet

network: dict = {}


def set_network(network_object) -> dict:
    """Set what network you want to use in the crypto library

    Args:
        network_object (dict): testnet or mainnet
    """
    global network
    network = {
        "epoch": network_object.epoch,
        "version": network_object.version,
        "wif": network_object.wif,
    }


def get_network() -> dict:
    """Get settings for a selected network, default network is testnet

    Returns:
        dict: network settings (default network is testnet)
    """
    if not network:
        set_network(Testnet)
    return network


def set_custom_network(epoch: datetime, version: int, wif: int) -> None:
    """Set custom network

    Args:
        epoch (datetime): chains epoch time
        version (int): chains version
        wif (int): chains wif
    """
    global network
    network = {
        "epoch": epoch,
        "version": version,
        "wif": wif,
    }


def get_network_version() -> int:
    """Get network version of the currently set network

    Returns:
        int: network version
    """
    network = get_network()
    return network["version"]
