from collections import OrderedDict

import pytest

from solar_crypto.configuration.network import set_network
from solar_crypto.constants import SOLAR_TRANSACTION_VOTE, TRANSACTION_TYPE_GROUP
from solar_crypto.exceptions import SolarInvalidTransaction
from solar_crypto.networks.testnet import Testnet
from solar_crypto.transactions.builder.vote import Vote, sort_votes

set_network(Testnet)


def test_vote_transaction_input_error():
    vote = {"deadlock": 50.3333}

    transaction = Vote()
    with pytest.raises(SolarInvalidTransaction) as e:
        transaction.set_votes(vote)
    assert str(e.value) == "Only two decimal places are allowed."


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
    assert transaction_dict["fee"] == 9000000

    transaction.verify()  # if no exception is raised, it means the transaction is valid


def test_vote_transaction_using_empty_list():
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
    assert transaction_dict["fee"] == 9000000

    transaction.verify()  # if no exception is raised, it means the transaction is valid


def test_vote_transaction_using_list_ok():
    transaction = Vote()
    transaction.set_votes(["awesome", "possom", "flossom"])
    transaction.set_nonce(1)
    transaction.sign("testing")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert OrderedDict(transaction_dict["asset"]["votes"]) == OrderedDict({
        "awesome": 33.34,
        "flossom": 33.33,
        "possom": 33.33,
    })
    assert transaction_dict["type"] is SOLAR_TRANSACTION_VOTE
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.SOLAR.value
    assert transaction_dict["fee"] == 9000000

    transaction.verify()  # if no exception is raised, it means the transaction is valid


def test_vote_transaction_using_list_more_than_53():
    transaction = Vote()

    with pytest.raises(SolarInvalidTransaction) as e:
        transaction.set_votes([str(x) for x in range(55)])
    assert str(e.value) == "Unable to vote for more than 53 delegates"


def test_sort_votes():
    votes = {
        "ddd": 50,
        "aaa": 15,
        "bbb": 15,
        "ccc": 20,
    }

    votes_sorted = sort_votes(votes)
    assert OrderedDict(votes_sorted) == OrderedDict({"ddd": 50, "ccc": 20, "aaa": 15, "bbb": 15})
