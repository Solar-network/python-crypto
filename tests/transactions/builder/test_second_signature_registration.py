import pytest

from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_SECOND_SIGNATURE_REGISTRATION, TRANSACTION_TYPE_GROUP
from crypto.networks.testnet import Testnet
from crypto.transactions.builder.second_signature_registration import SecondSignatureRegistration

set_network(Testnet)


@pytest.mark.parametrize("version", [2, 3])
def test_second_signature_registration_transaction(version):
    """Test if a second signature registration transaction gets built"""
    transaction = SecondSignatureRegistration("this is a top secret passphrase")
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.sign("testing")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["type"] is TRANSACTION_SECOND_SIGNATURE_REGISTRATION
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict["fee"] == 5000000

    transaction.verify()  # if no exception is raised, it means the transaction is valid


@pytest.mark.parametrize("version", [2, 3])
def test_second_signature_registration_transaction_custom_fee(version):
    """Test if a second signature registration transaction gets built with a custom fee"""
    transaction = SecondSignatureRegistration("this is a top secret passphrase", 5)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.sign("testing")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["type"] is TRANSACTION_SECOND_SIGNATURE_REGISTRATION
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict["fee"] == 5

    transaction.verify()  # if no exception is raised, it means the transaction is valid
