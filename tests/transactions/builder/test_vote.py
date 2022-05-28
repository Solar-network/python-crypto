import pytest

from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_TYPE_GROUP, TRANSACTION_VOTE
from crypto.networks.testnet import Testnet
from crypto.transactions.builder.vote import Vote

set_network(Testnet)


@pytest.mark.parametrize("version", [2, 3])
def test_vote_transaction_with_pubkey(version):
    """Test if a vote transaction gets built"""
    vote = "+034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192"

    transaction = Vote()
    transaction.set_votes([vote])
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.sign("testing")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["asset"]["votes"]
    assert transaction_dict["type"] is TRANSACTION_VOTE
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict["fee"] == 100000000

    transaction.verify()  # if no exception is raised, it means the transaction is valid


@pytest.mark.parametrize("version", [2, 3])
def test_vote_transaction_with_username(version):
    """Test if a vote transaction gets built"""

    transaction = Vote()
    transaction.set_votes(["+asterix"])
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.sign("testing")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["asset"]["votes"]
    assert transaction_dict["type"] is TRANSACTION_VOTE
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict["fee"] == 100000000

    transaction.verify()  # if no exception is raised, it means the transaction is valid


@pytest.mark.parametrize("version", [2, 3])
def test_vote_switch_transaction_with_username(version):
    """Test if a vote transaction gets built"""

    transaction = Vote()
    transaction.set_votes(["-obelix", "+asterix"])
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.sign("testing")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["asset"]["votes"]
    assert transaction_dict["type"] is TRANSACTION_VOTE
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict["fee"] == 100000000

    transaction.verify()  # if no exception is raised, it means the transaction is valid


@pytest.mark.parametrize("version", [2, 3])
def test_vote_transaction_custom_fee(version):
    """Test if a vote transaction gets built with a custom fee"""
    vote = "+034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192"

    transaction = Vote(None, 5)
    transaction.set_votes([vote])
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.sign("testing")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["asset"]["votes"]
    assert transaction_dict["type"] is TRANSACTION_VOTE
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict["fee"] == 5

    transaction.verify()  # if no exception is raised, it means the transaction is valid
