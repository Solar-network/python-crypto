from hashlib import sha256
import pytest

from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_HTLC_LOCK, TRANSACTION_TYPE_GROUP
from crypto.networks.testnet import Testnet
from crypto.transactions.builder.htlc_lock import HtlcLock

set_network(Testnet)


def test_htlc_lock_transation_amount_not_int():
    with pytest.raises(ValueError):
        """Test error handling in constructor for non-integer amount
        """
        secret_hash = _generate_secret_hash()
        HtlcLock(
            recipient_id='DEMvpU4Qq6KvSzF3sRNjGCkm6Kj7cFfVaz',
            amount='bad amount number',
            secret_hash=secret_hash,
            expiration_type=1,
            expiration_value=1573455822
        )


def test_htlc_lock_transation_amount_zero():
    with pytest.raises(ValueError):
        """Test error handling in constructor for non-integer amount
        """
        secret_hash = _generate_secret_hash()
        HtlcLock(
          recipient_id='DEMvpU4Qq6KvSzF3sRNjGCkm6Kj7cFfVaz',
          amount=0,
          secret_hash=secret_hash,
          expiration_type=1,
          expiration_value=1573455822
        )


def test_htlc_lock_transation_amount_negative():
    with pytest.raises(ValueError):
        """Test error handling in constructor for non-integer amount
        """
        secret_hash = _generate_secret_hash()
        HtlcLock(
          recipient_id='DEMvpU4Qq6KvSzF3sRNjGCkm6Kj7cFfVaz',
          amount=-5,
          secret_hash=secret_hash,
          expiration_type=1,
          expiration_value=1573455822
        )


@pytest.mark.parametrize("version", [2, 3])
def test_htlc_lock_transaction(version):
    """Test if timelock transaction gets built
    """
    secret_hash = _generate_secret_hash()
    transaction = HtlcLock(
      recipient_id='DEMvpU4Qq6KvSzF3sRNjGCkm6Kj7cFfVaz',
      amount=200000000,
      secret_hash=secret_hash,
      expiration_type=1,
      expiration_value=1573455822
    )

    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.sign('this is a random passphrase')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['recipientId'] == 'DEMvpU4Qq6KvSzF3sRNjGCkm6Kj7cFfVaz'
    assert transaction_dict['amount'] == 200000000
    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_HTLC_LOCK
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 10000000
    assert transaction_dict['asset']['lock']['secretHash'] == secret_hash
    assert transaction_dict['asset']['lock']['expiration']['type'] == 1
    assert transaction_dict['asset']['lock']['expiration']['value'] == 1573455822

    transaction.verify()  # if no exception is raised, it means the transaction is valid


@pytest.mark.parametrize("version", [2, 3])
def test_htlc_lock_transaction_custom_fee(version):
    """Test if timelock transaction gets built with a custom fee
    """
    secret_hash = _generate_secret_hash()
    transaction = HtlcLock(
      recipient_id='DEMvpU4Qq6KvSzF3sRNjGCkm6Kj7cFfVaz',
      amount=200000000,
      secret_hash=secret_hash,
      expiration_type=1,
      expiration_value=1573455822,
      fee=5
    )

    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.set_version(version)
    transaction.sign('testing')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['recipientId'] == 'DEMvpU4Qq6KvSzF3sRNjGCkm6Kj7cFfVaz'
    assert transaction_dict['amount'] == 200000000
    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_HTLC_LOCK
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 5
    assert transaction_dict['asset']['lock']['secretHash'] == secret_hash
    assert transaction_dict['asset']['lock']['expiration']['type'] == 1
    assert transaction_dict['asset']['lock']['expiration']['value'] == 1573455822

    transaction.verify()  # if no exception is raised, it means the transaction is valid


def _generate_secret_hash():
  secret = "super secret code that must be unique and entirely random"

  # secret code is a key ingredient used to unlock the htlc lock. To generate an unlock code one
  # must "hexify" it: `unlock_secret = hexlify(secret_h.encode()).decode()``
  secret_code = sha256(secret.encode()).digest()[:32]

  # secret_hash is the hashed secret code
  secret_hash = sha256(secret_code).hexdigest()
  return secret_hash
