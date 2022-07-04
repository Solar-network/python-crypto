import inspect
from binascii import hexlify, unhexlify
from importlib import import_module

from binary.unsigned_integer.reader import read_bit8, read_bit16, read_bit32, read_bit64

from solar_crypto.constants import (
    SOLAR_TRANSACTION_TYPES,
    TRANSACTION_TYPE_GROUP,
    TRANSACTION_TYPES,
)
from solar_crypto.exceptions import SolarDeserializerException, SolarSerializerException
from solar_crypto.identity import address
from solar_crypto.transactions.deserializers.base import BaseDeserializer


class Deserializer(object):

    serialized = None

    def __init__(self, serialized):
        self.serialized = unhexlify(serialized)

    def deserialize(self):
        """Deserialize transaction

        Returns:
            object: returns Transaction resource object
        """
        # circular import with transaction.py :( - I'm thinking of just returning a dict here
        # which then needs to be passed to a Transaction object, instead of returning a Transaction
        # object
        from solar_crypto.transactions.transaction import Transaction

        transaction = Transaction()
        transaction.version = read_bit8(self.serialized, offset=1)
        transaction.network = read_bit8(self.serialized, offset=2)
        transaction.typeGroup = read_bit32(self.serialized, offset=3)
        transaction.type = read_bit16(self.serialized, offset=7)
        transaction.nonce = read_bit64(self.serialized, offset=9)
        transaction.senderPublicKey = hexlify(self.serialized)[34 : 66 + 34].decode()
        transaction.fee = read_bit64(self.serialized, offset=50)

        memo_length = read_bit8(self.serialized, offset=58)
        if memo_length > 0:
            memo_offset = 59
            memo_end = memo_offset + memo_length
            transaction.memo = self.serialized[memo_offset:memo_end].decode()

        asset_offset = (58 + 1) * 2 + memo_length * 2
        handled_transaction = self._handle_transaction_type(asset_offset, transaction)
        transaction.amount = handled_transaction.amount
        transaction.version = handled_transaction.version

        if transaction.version not in [2, 3]:
            raise SolarDeserializerException(
                "%s is not a valid transaction version", transaction.version
            )

        self._validate(transaction)

        return transaction

    def _handle_transaction_type(self, asset_offset, transaction):
        """Handle deserialization for a given transaction type

        Args:
            asset_offset (int):
            transaction (object): Transaction resource object

        Returns:
            object: Transaction resource object of currently deserialized data
        """
        deserializer_name = self._get_deserializer_name(transaction)
        module = import_module(
            "solar_crypto.transactions.deserializers.{}".format(deserializer_name)
        )
        for attr in dir(module):
            # If attr name is `BaseDeserializer`, skip it as it's a class and also has a
            # subclass of BaseDeserializer
            if attr == "BaseDeserializer":
                continue

            attribute = getattr(module, attr)
            if inspect.isclass(attribute) and issubclass(attribute, BaseDeserializer):
                # this attribute is actually a specific deserializer that we want to use
                deserializer = attribute
                break
        return deserializer(self.serialized, asset_offset, transaction).deserialize()

    @staticmethod
    def _get_deserializer_name(transaction):
        if transaction.typeGroup == TRANSACTION_TYPE_GROUP.SOLAR.value:
            name = SOLAR_TRANSACTION_TYPES[transaction.type]
        else:
            name = TRANSACTION_TYPES[transaction.type]
        return name

    @staticmethod
    def _validate(transaction):
        if not transaction.recipientId:
            return

        if not address.validate_address(transaction.recipientId):
            raise SolarSerializerException("Invalid recipient address")
