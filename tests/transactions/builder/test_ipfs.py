import pytest
from base58 import b58encode

from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_IPFS, TRANSACTION_TYPE_GROUP
from crypto.networks.testnet import Testnet
from crypto.transactions.builder.ipfs import IPFS

set_network(Testnet)


@pytest.mark.parametrize("version", [2, 3])
def test_ipfs_transaction(version):
    """Test if ipfs transaction gets built"""
    ipfs_cid = "QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4"

    transaction = IPFS(ipfs_cid)
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.sign("testing")
    transaction_dict = transaction.to_dict()
    transaction.to_json()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["type"] is TRANSACTION_IPFS
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict["fee"] == 500000000
    assert transaction_dict["asset"]["ipfs"] == ipfs_cid

    transaction.verify()  # if no exception is raised, it means the transaction is valid


@pytest.mark.parametrize("version", [2, 3])
def test_ipfs_transaction_custom_fee(version):
    """Test if ipfs transaction gets built with custom fee"""
    ipfs_cid = "QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4"

    transaction = IPFS()
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.set_ipfs_cid(ipfs_cid)
    transaction.sign("testing")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["type"] is TRANSACTION_IPFS
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict["asset"]["ipfs"] == ipfs_cid

    transaction.verify()  # if no exception is raised, it means the transaction is valid
