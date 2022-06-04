import pytest

from solar_crypto.configuration.network import set_network
from solar_crypto.constants import TRANSACTION_DELEGATE_RESIGNATION, TRANSACTION_TYPE_GROUP
from solar_crypto.networks.testnet import Testnet
from solar_crypto.transactions.builder.delegate_resignation import DelegateResignation

set_network(Testnet)


@pytest.mark.parametrize("version", [2, 3])
def test_delegate_resignation_transaction(version):
    """Test if delegate resignation transaction gets built"""
    transaction = DelegateResignation()
    transaction.set_nonce(1)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_version(version)
    transaction.sign("testing")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["type"] is TRANSACTION_DELEGATE_RESIGNATION
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict["fee"] == 0

    transaction.verify()  # if no exception is raised, it means the transaction is valid


@pytest.mark.parametrize("version", [2, 3])
def test_delegate_resignation_with_vendor_field_transaction(version):
    """Test if delegate resignation transaction gets built"""
    transaction = DelegateResignation()
    transaction.set_nonce(1)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_version(version)
    transaction.set_vendor_field("bye mr delegate")
    transaction.sign("testing")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["vendorField"] == "bye mr delegate"
    assert transaction_dict["type"] is TRANSACTION_DELEGATE_RESIGNATION
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict["fee"] == 0

    transaction.verify()  # if no exception is raised, it means the transaction is valid


@pytest.mark.parametrize("version", [2, 3])
def test_delegate_resignation_transaction_custom_fee(version):
    """Test if delegate resignation transaction gets built with a custom fee"""
    transaction = DelegateResignation(5)
    transaction.set_nonce(1)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_version(version)
    transaction.sign("testing")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["type"] is TRANSACTION_DELEGATE_RESIGNATION
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict["fee"] == 5

    transaction.verify()  # if no exception is raised, it means the transaction is valid
