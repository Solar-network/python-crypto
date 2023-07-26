from typing import Union

from solar_crypto.configuration.fee import get_fee
from solar_crypto.constants import HTLC_LOCK_EXPIRATION_TYPE, TRANSACTION_TYPE_GROUP
from solar_crypto.identity.private_key import PrivateKey
from solar_crypto.identity.public_key import PublicKey
from solar_crypto.transactions.transaction import Transaction
from solar_crypto.utils.crypto import sign_schnorr, sign_schnorr_legacy


class BaseTransactionBuilder(object):
    def __init__(self):
        self.transaction = Transaction()
        self.transaction.type = getattr(self, "transaction_type", None)
        self.transaction.fee = get_fee(
            getattr(self, "transaction_type", None), getattr(self, "typeGroup", 1)
        )
        self.transaction.nonce = getattr(self, "nonce", None)
        self.transaction.typeGroup = getattr(self, "typeGroup", 1)
        self.transaction.signatures = getattr(self, "signatures", None)
        self.transaction.version = getattr(self, "version", 3)
        if self.transaction.type != 0:
            self.transaction.amount = getattr(self, "amount", 0)

    def to_dict(self) -> dict:
        return self.transaction.to_dict()

    def to_json(self) -> str:
        return self.transaction.to_json()

    def sign(self, passphrase: str):
        """Sign the transaction using the given passphrase

        Args:
            passphrase (str): passphrase associated with the address sending this transaction
        """
        pvt = PrivateKey.from_passphrase(passphrase)
        self.transaction.senderPublicKey = PublicKey.from_passphrase(passphrase)
        msg = self.transaction.to_bytes(True, True, False)

        if self.transaction.version > 2:
            # schnorr bip340
            sig = sign_schnorr(msg, pvt)
            self.transaction.signature = sig
            self.transaction.id = self.transaction.get_id()
        else:
            # schnorr legacy
            sig = sign_schnorr_legacy(msg, pvt)
            self.transaction.signature = sig
            self.transaction.id = self.transaction.get_id()

    def second_sign(self, passphrase: str):
        """Sign the transaction using the given second passphrase

        Args:
            passphrase (str): 2nd passphrase associated with the address sending this transaction
        """
        pvt = PrivateKey.from_passphrase(passphrase)
        msg = self.transaction.to_bytes(False, True, False)

        if self.transaction.version > 2:
            # schnorr bip340
            sig = sign_schnorr(msg, pvt)
            self.transaction.signSignature = sig
            self.transaction.id = self.transaction.get_id()
        else:
            # schnorr legacy
            sig = sign_schnorr_legacy(msg, pvt)
            self.transaction.signSignature = sig
            self.transaction.id = self.transaction.get_id()

    def multi_sign(self, passphrase: str, index: int):
        """Sign the transaction with one of multiple signatures

        Args:
            passphrase (str): passphrase signing the transaction
            index (int): index of the passphrase signing the transaction
        """
        if not self.transaction.signatures:
            self.transaction.signatures = []

        index = len(self.transaction.signatures) if index == -1 else index
        pvt = PrivateKey.from_passphrase(passphrase)
        index_formatted = hex(index).replace("x", "")
        msg = self.transaction.to_bytes(True, True, True)

        if self.transaction.version > 2:
            # schnorr bip340
            sig = sign_schnorr(msg, pvt)
            indexed_signature = f"{index_formatted}{sig}"
            self.transaction.signatures.append(indexed_signature)
        else:
            # schnorr legacy
            sig = sign_schnorr_legacy(msg, pvt)
            self.transaction.signatures.append(f"{index_formatted}{sig}")

    def verify(self) -> bool:
        return self.transaction.verify()

    def verify_second(self, secondPublicKey: str) -> bool:
        return self.transaction.verify_secondsig(secondPublicKey)

    def verify_multisig(self, multi_signature_asset: dict) -> bool:
        return self.transaction.verify_signatures(multi_signature_asset)

    def set_nonce(self, nonce: int):
        self.transaction.nonce = nonce

    def set_fee(self, fee: int):
        self.transaction.fee = fee

    def set_amount(self, amount: int):
        self.transaction.amount = amount

    def set_sender_public_key(self, public_key: str):
        self.transaction.senderPublicKey = public_key

    def set_expiration(self, expiration: HTLC_LOCK_EXPIRATION_TYPE):
        """Set HTLC expiration

        Args:
            expiration (HTLC_LOCK_EXPIRATION_TYPE)
        """
        if type(expiration) == int:
            self.transaction.expiration = expiration
        else:
            types = {
                HTLC_LOCK_EXPIRATION_TYPE.EPOCH_TIMESTAMP: 1,
                HTLC_LOCK_EXPIRATION_TYPE.BLOCK_HEIGHT: 2,
            }
            self.transaction.expiration = types[expiration]

    def set_type_group(self, type_group: Union[int, TRANSACTION_TYPE_GROUP]):
        if isinstance(type_group, TRANSACTION_TYPE_GROUP):
            self.transaction.typeGroup = int(type_group)
        else:
            self.transaction.typeGroup = type_group

    def set_version(self, version: int):
        self.transaction.version = version

    def set_memo(self, value: str):
        """Set memo value

        Args:
            value (str)
        """
        self.transaction.memo = value.encode()
