import pytest

from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_TRANSFER, TRANSACTION_TYPE_GROUP
from crypto.identity.public_key import PublicKey
from crypto.networks.testnet import Testnet
from crypto.transactions.builder.transfer import Transfer

set_network(Testnet)


@pytest.mark.parametrize("version", [2, 3])
def test_transfer_transaction(version):
    """Test if a transfer transaction gets built"""
    transaction = Transfer(
        recipientId="D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib",
        amount=200000000,
    )
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.sign("this is a top secret passphrase")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["version"] == version
    assert transaction_dict["type"] is TRANSACTION_TRANSFER
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict["fee"] == 5000000

    transaction.verify()  # if no exception is raised, it means the transaction is valid


@pytest.mark.parametrize("version", [2, 3])
def test_transfer_transaction_with_vendor_field(version):
    """Test if a transfer transaction gets built"""
    transaction = Transfer(
        recipientId="D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib",
        amount=200000000,
    )
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_vendor_field("hello world")
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.sign("this is a top secret passphrase")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["vendorField"] == "hello world"
    assert transaction_dict["version"] == version
    assert transaction_dict["type"] is TRANSACTION_TRANSFER
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict["fee"] == 5000000

    transaction.verify()  # if no exception is raised, it means the transaction is valid


@pytest.mark.parametrize("version", [2, 3])
def test_transfer_transaction_update_amount(version):
    """Test if a transfer transaction can update an amount"""
    transaction = Transfer(recipientId="D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib", amount=200000000)
    transaction.set_amount(10)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.sign("this is a top secret passphrase")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["version"] == version
    assert transaction_dict["type"] is TRANSACTION_TRANSFER
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict["amount"] == 10

    transaction.verify()  # if no exception is raised, it means the transaction is valid


@pytest.mark.parametrize("version", [2, 3])
def test_transfer_transaction_custom_fee_via_kwargs(version):
    """Test if a transfer transaction gets built with a custom fee
    """
    transaction = Transfer(
        recipientId="D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib", amount=200000000, fee=5
    )
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.sign("this is a top secret passphrase")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["type"] is TRANSACTION_TRANSFER
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict["fee"] == 5

    transaction.verify()  # if no exception is raised, it means the transaction is valid


@pytest.mark.parametrize("version", [2, 3])
def test_transfer_transaction_custom_fee_via_method(version):
    """Test if a transfer transaction gets built with a custom fee
    """
    transaction = Transfer(
        recipientId='D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib',
        amount=200000000,
    )
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.set_fee(1337)
    transaction.set_version(version)
    transaction.sign('this is a top secret passphrase')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_TRANSFER
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 1337

    transaction.verify()  # if no exception is raised, it means the transaction is valid


@pytest.mark.parametrize("version", [2, 3])
def test_transfer_secondsig_transaction(version):
    """Test if a transfer transaction with second signature gets built"""
    transaction = Transfer(
        recipientId="D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib",
        amount=200000000,
    )
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.sign("this is a top secret passphrase")
    transaction.second_sign("second top secret passphrase")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["signSignature"]
    assert transaction_dict["type"] is TRANSACTION_TRANSFER
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.CORE.value

    transaction.verify()  # if no exception is raised, it means the transaction is valid
    transaction.verify_second(
        PublicKey.from_passphrase("second top secret passphrase")
    )  # if no exception is raised, it means the transaction is valid


def test_parse_signatures(transaction_type_0):
    """Test if parse signature works when parsing serialized data"""
    transfer = Transfer(
        recipientId=transaction_type_0["recipientId"], amount=transaction_type_0["amount"]
    )
    assert transfer.transaction.signature is None
    transfer.transaction.parse_signatures(transaction_type_0["serialized"], 166)
    assert transfer.transaction.signature


def test_transfer_transaction_amount_not_int():
    with pytest.raises(ValueError):
        """Test error handling in constructor for non-integer amount"""
        Transfer(recipientId="D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib", amount="bad amount")


def test_transfer_transaction_amount_zero():
    with pytest.raises(ValueError):
        """Test error handling in constructor for non-integer amount"""
        Transfer(recipientId="D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib", amount=0)


def test_transfer_transaction_invalid_address():
    with pytest.raises(ValueError):
        """Test error handling in constructor for non-integer amount"""
        Transfer(recipientId="AGeYmgbg2LgGxRW2vNNJvQ88PknEJsYizC", amount=12421421)
