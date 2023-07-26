import pytest

from solar_crypto.configuration.network import set_network
from solar_crypto.constants import TRANSACTION_TRANSFER, TRANSACTION_TYPE_GROUP
from solar_crypto.networks.testnet import Testnet
from solar_crypto.transactions.builder.transfer import Transfer

set_network(Testnet)


@pytest.mark.parametrize("version", [2, 3])
def test_transaction(version):
    """Test if transfer transaction gets built"""
    transaction = Transfer()
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.add_transfer(1, "D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib")
    transaction.add_transfer(2, "DNSBvFTJtQpS4hJfLerEjSXDrBT7K6HL2o")
    transaction.set_version(version)
    transaction.sign("testing")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["type"] is TRANSACTION_TRANSFER
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict["fee"] == 50000000
    assert transaction_dict["asset"]["transfers"][0]["amount"] == 1
    assert (
        transaction_dict["asset"]["transfers"][0]["recipientId"]
        == "D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib"
    )
    assert transaction_dict["asset"]["transfers"][1]["amount"] == 2
    assert (
        transaction_dict["asset"]["transfers"][1]["recipientId"]
        == "DNSBvFTJtQpS4hJfLerEjSXDrBT7K6HL2o"
    )

    transaction.verify()  # if no exception is raised, it means the transaction is valid


@pytest.mark.parametrize("version", [2, 3])
def test_transaction_custom_fee_via_kwargs(version):
    """Test if transfer transaction gets built with a custom fee"""
    transaction = Transfer(fee=5)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.add_transfer(1, "D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib")
    transaction.add_transfer(2, "DNSBvFTJtQpS4hJfLerEjSXDrBT7K6HL2o")
    transaction.sign("testing")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["type"] is TRANSACTION_TRANSFER
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict["fee"] == 5
    assert transaction_dict["asset"]["transfers"][0]["amount"] == 1
    assert (
        transaction_dict["asset"]["transfers"][0]["recipientId"]
        == "D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib"
    )
    assert transaction_dict["asset"]["transfers"][1]["amount"] == 2
    assert (
        transaction_dict["asset"]["transfers"][1]["recipientId"]
        == "DNSBvFTJtQpS4hJfLerEjSXDrBT7K6HL2o"
    )

    transaction.verify()  # if no exception is raised, it means the transaction is valid


@pytest.mark.parametrize("version", [2, 3])
def test_transaction_custom_fee_via_method(version):
    """Test if transfer transaction gets built with a custom fee"""
    transaction = Transfer()
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.set_fee(1337)
    transaction.add_transfer(1, "D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib")
    transaction.add_transfer(2, "DNSBvFTJtQpS4hJfLerEjSXDrBT7K6HL2o")
    transaction.sign("testing")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["type"] is TRANSACTION_TRANSFER
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict["fee"] == 1337
    assert transaction_dict["asset"]["transfers"][0]["amount"] == 1
    assert (
        transaction_dict["asset"]["transfers"][0]["recipientId"]
        == "D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib"
    )
    assert transaction_dict["asset"]["transfers"][1]["amount"] == 2
    assert (
        transaction_dict["asset"]["transfers"][1]["recipientId"]
        == "DNSBvFTJtQpS4hJfLerEjSXDrBT7K6HL2o"
    )

    transaction.verify()  # if no exception is raised, it means the transaction is valid


def test_transaction_one_transfer():
    """Test if transfer works with one transfer"""
    transaction = Transfer()
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.set_version(3)
    transaction.set_fee(1337)
    transaction.add_transfer(1, "D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib")
    transaction.sign("testing")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["type"] is TRANSACTION_TRANSFER
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict["fee"] == 1337
    assert transaction_dict["asset"]["transfers"][0]["amount"] == 1
    assert (
        transaction_dict["asset"]["transfers"][0]["recipientId"]
        == "D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib"
    )

    transaction.verify()  # if no exception is raised, it means the transaction is valid
