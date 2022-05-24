import pytest

from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_DELEGATE_REGISTRATION, TRANSACTION_TYPE_GROUP
from crypto.networks.testnet import Testnet
from crypto.transactions.builder.delegate_registration import DelegateRegistration

set_network(Testnet)


@pytest.mark.parametrize("version", [2, 3])
def test_delegate_registration_transaction(version):
    """Test if a delegate registration transaction gets built
    """
    delegate_name = 'mr.delegate'

    transaction = DelegateRegistration(delegate_name)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.sign('testing')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['asset']['delegate']['username'] == delegate_name
    assert transaction_dict['type'] is TRANSACTION_DELEGATE_REGISTRATION
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 2500000000

    transaction.verify()  # if no exception is raised, it means the transaction is valid


@pytest.mark.parametrize("version", [2, 3])
def test_delegate_registration_transaction_custom_fee(version):
    """Test if a delegate registration transaction gets built with a custom fee
    """
    delegate_name = 'mr.delegate'

    transaction = DelegateRegistration(delegate_name, 5)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.sign('testing')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['asset']['delegate']['username'] == delegate_name
    assert transaction_dict['type'] is TRANSACTION_DELEGATE_REGISTRATION
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 5

    transaction.verify()  # if no exception is raised, it means the transaction is valid
