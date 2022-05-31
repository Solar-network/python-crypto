import binascii

import pytest

from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_HTLC_CLAIM, TRANSACTION_TYPE_GROUP, HashingType
from crypto.networks.testnet import Testnet
from crypto.transactions.builder.htlc_claim import HtlcClaim

set_network(Testnet)


@pytest.mark.parametrize("version", [2, 3])
def test_htlc_claim_transaction_ok(version):
    """Test if timelock transaction gets built"""
    lock_transaction_id = "943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4"

    # Secret required to unlock and claim funds from an HTLC. This secret should is revealed to you
    # on the blockchain which you can then use to claim funds.
    unlock_secret = "1e9f2bbccc07c643316be6faae9f004cc16dec3910501387fd326cd8a39b4fdb"

    transaction = HtlcClaim(lock_transaction_id, unlock_secret, HashingType.SHA256)
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.sign("testing")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["type"] is TRANSACTION_HTLC_CLAIM
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict["fee"] == 0
    assert (
        transaction_dict["asset"]["claim"]["lockTransactionId"]
        == "943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4"
    )
    assert transaction_dict["asset"]["claim"]["unlockSecret"] == unlock_secret

    transaction.verify()  # if no exception is raised, it means the transaction is valid


@pytest.mark.parametrize("version", [2, 3])
def test_htlc_claim_transaction_unlock_secret_not_hex(version):
    """Test if timelock transaction errors if an invalid hex unlock_secret is given"""
    lock_transaction_id = "943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4"

    # Secret required to unlock and claim funds from an HTLC. This secret should is revealed to you
    # on the blockchain which you can then use to claim funds.
    unlock_secret = "643432323362663933653230323530356136613530313432316138a84a3966x1"

    transaction = HtlcClaim(lock_transaction_id, unlock_secret)
    transaction.set_version(version)
    transaction.set_nonce(1)
    with pytest.raises(binascii.Error) as e:
        transaction.sign("testing")
    assert str(e.value) == "Non-hexadecimal digit found"


@pytest.mark.parametrize("version", [2, 3])
def test_htlc_claim_transaction_custom_fee_ok(version):
    """Test if timelock transaction gets built with a custom fee"""
    lock_transaction_id = "943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4"

    # Secret required to unlock and claim funds from an HTLC. This secret should is revealed to you
    # on the blockchain which you can then use to claim funds.
    unlock_secret = "1e9f2bbccc07c643316be6faae9f004cc16dec3910501387fd326cd8a39b4fdb"

    transaction = HtlcClaim(lock_transaction_id, unlock_secret, fee=5)
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.sign("testing")
    transaction_dict = transaction.to_dict()

    assert transaction_dict["nonce"] == 1
    assert transaction_dict["signature"]
    assert transaction_dict["type"] is TRANSACTION_HTLC_CLAIM
    assert transaction_dict["typeGroup"] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict["fee"] == 5
    assert (
        transaction_dict["asset"]["claim"]["lockTransactionId"]
        == "943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4"
    )
    assert transaction_dict["asset"]["claim"]["unlockSecret"] == unlock_secret

    transaction.verify()  # if no exception is raised, it means the transaction is valid
