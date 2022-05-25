import pytest

from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_MULTI_PAYMENT, TRANSACTION_TYPE_GROUP
from crypto.networks.testnet import Testnet
from crypto.transactions.builder.multi_payment import MultiPayment

set_network(Testnet)


@pytest.mark.parametrize("version", [2, 3])
def test_multi_payment_transaction(version):
    """Test if multi payment transaction gets built
    """
    transaction = MultiPayment()
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.add_payment(1, 'DEMvpU4Qq6KvSzF3sRNjGCkm6Kj7cFfVaz')
    transaction.add_payment(2, 'DQveGkK7te33dWJwHgKpGKDr5amxAE7PF4')
    transaction.set_version(version)
    transaction.sign('testing')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_MULTI_PAYMENT
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 10000000
    assert transaction_dict['asset']['payments'][0]['amount'] == 1
    assert transaction_dict['asset']['payments'][0]['recipientId'] == 'DEMvpU4Qq6KvSzF3sRNjGCkm6Kj7cFfVaz'
    assert transaction_dict['asset']['payments'][1]['amount'] == 2
    assert transaction_dict['asset']['payments'][1]['recipientId'] == 'DQveGkK7te33dWJwHgKpGKDr5amxAE7PF4'

    transaction.verify()  # if no exception is raised, it means the transaction is valid


@pytest.mark.parametrize("version", [2, 3])
def test_multi_payment_transaction_custom_fee(version):
    """Test if multi payment transaction gets built with a custom fee
    """
    transaction = MultiPayment(fee=5)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.add_payment(1, 'DEMvpU4Qq6KvSzF3sRNjGCkm6Kj7cFfVaz')
    transaction.add_payment(2, 'DQveGkK7te33dWJwHgKpGKDr5amxAE7PF4')
    transaction.sign('testing')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_MULTI_PAYMENT
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 5
    assert transaction_dict['asset']['payments'][0]['amount'] == 1
    assert transaction_dict['asset']['payments'][0]['recipientId'] == 'DEMvpU4Qq6KvSzF3sRNjGCkm6Kj7cFfVaz'
    assert transaction_dict['asset']['payments'][1]['amount'] == 2
    assert transaction_dict['asset']['payments'][1]['recipientId'] == 'DQveGkK7te33dWJwHgKpGKDr5amxAE7PF4'

    transaction.verify()  # if no exception is raised, it means the transaction is valid


@pytest.mark.parametrize("version", [2, 3])
def test_multi_payment_transaction_invalid_recipient(version):
    """Test if multi payment transaction gets built with a custom fee
    """
    transaction = MultiPayment(fee=5)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.add_payment(1, 'DEMvpU4Qq6KvSzF3sRNjGCkm6Kj7cFfVaz')
    with pytest.raises(ValueError):
        transaction.add_payment(2, 'AGeYmgbg2LgGxRW2vNNJvQ88PknEJsYizC')
