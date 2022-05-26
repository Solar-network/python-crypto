import pytest

from crypto.configuration.network import set_network
from crypto.constants import SOLAR_TRANSACTION_TYPES, SOLAR_TRANSACTION_BURN, SOLAR_TRANSACTION_FEES, TRANSACTION_TYPE_GROUP
from crypto.identity.public_key import PublicKey
from crypto.networks.testnet import Testnet
from crypto.transactions.builder.burn import Burn


set_network(Testnet)


@pytest.mark.parametrize("version", [2, 3])
def test_burn_transaction(version):
    """Test if a transfer transaction gets built
    """
    transaction = Burn(amount=200000000)
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.sign('this is a top secret passphrase')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['version'] == version
    assert transaction_dict['type'] is SOLAR_TRANSACTION_BURN
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.SOLAR.value
    assert transaction_dict['fee'] == SOLAR_TRANSACTION_FEES[SOLAR_TRANSACTION_BURN]

    transaction.verify()  # if no exception is raised, it means the transaction is valid


@pytest.mark.parametrize("version", [2, 3])
def test_burn_transaction_with_vendor_field(version):
    """Test if a transfer transaction gets built
    """
    transaction = Burn(amount=200000000)
    transaction.set_vendor_field("hello world")
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.sign('this is a top secret passphrase')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['vendorField'] == "hello world"
    assert transaction_dict['version'] == version
    assert transaction_dict['type'] is SOLAR_TRANSACTION_BURN
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.SOLAR.value
    assert transaction_dict['fee'] == SOLAR_TRANSACTION_FEES[SOLAR_TRANSACTION_BURN]

    transaction.verify()  # if no exception is raised, it means the transaction is valid
