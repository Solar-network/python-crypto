from binascii import hexlify, unhexlify

from base58 import b58encode_check
from binary.unsigned_integer.reader import read_bit8, read_bit32, read_bit64

from solar_crypto.transactions.deserializers.base import BaseDeserializer


class HtlcLockDeserializer(BaseDeserializer):
    def deserialize(self):
        starting_position = int(self.asset_offset / 2)
        offset = 0

        self.transaction.amount = read_bit64(self.serialized, offset=starting_position)
        offset += 8

        secret_hash_length = read_bit8(self.serialized, offset=starting_position + 8)
        offset += 1

        secret_hash = hexlify(self.serialized)[
            (starting_position + offset) * 2 : (starting_position + offset + secret_hash_length) * 2
        ]
        offset += secret_hash_length

        expiration_type = read_bit8(self.serialized, offset=starting_position + offset)
        offset += 1

        expiration_value = read_bit32(self.serialized, offset=starting_position + offset)
        offset += 4

        recipient_start_index = (starting_position + offset) * 2
        recipientId = hexlify(self.serialized)[recipient_start_index : recipient_start_index + 42]
        self.transaction.recipientId = b58encode_check(unhexlify(recipientId)).decode()
        offset += 21

        self.transaction.asset["lock"] = {"secretHash": secret_hash.decode()}

        self.transaction.asset["lock"]["expiration"] = {
            "type": expiration_type,
            "value": expiration_value,
        }

        self.transaction.parse_signatures(
            hexlify(self.serialized).decode(), self.asset_offset + (offset * 2)
        )

        return self.transaction
