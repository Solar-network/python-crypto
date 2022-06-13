from solar_crypto.configuration.network import set_network
from solar_crypto.constants import SOLAR_TRANSACTION_VOTE, TRANSACTION_TYPE_GROUP
from solar_crypto.networks.testnet import Testnet
from solar_crypto.transactions.builder.vote import Vote

set_network(Testnet)


def test_vote_transaction():
    vote = {"deadlock": 50.3333}

    transaction = Vote()
    transaction.set_votes(vote)
    transaction.set_nonce(1)
    transaction.sign("testing")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["asset"]["votes"] == vote
    assert transaction_dict["type"] is SOLAR_TRANSACTION_VOTE
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.SOLAR.value
    assert transaction_dict["fee"] == 100000000

    transaction.verify()  # if no exception is raised, it means the transaction is valid


def test_vote_transaction_multiple_votes():
    vote = {"fun": 35.3, "deadlock": 64.7}

    transaction = Vote()
    transaction.set_votes(vote)
    transaction.set_nonce(1)
    transaction.sign("testing")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["asset"]["votes"] == vote
    assert transaction_dict["type"] is SOLAR_TRANSACTION_VOTE
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.SOLAR.value
    assert transaction_dict["fee"] == 100000000

    transaction.verify()  # if no exception is raised, it means the transaction is valid


def test_vote_transaction_multiple_votes():
    transaction = Vote()
    transaction.set_votes(["-awesome"])
    transaction.set_nonce(1)
    transaction.sign("testing")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["asset"]["votes"] == {}
    assert transaction_dict["type"] is SOLAR_TRANSACTION_VOTE
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.SOLAR.value
    assert transaction_dict["fee"] == 100000000

    transaction.verify()  # if no exception is raised, it means the transaction is valid
