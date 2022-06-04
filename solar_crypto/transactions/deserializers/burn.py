from binascii import hexlify

from binary.unsigned_integer.reader import read_bit64

from solar_crypto.transactions.deserializers.base import BaseDeserializer


class BurnDeserializer(BaseDeserializer):
    def deserialize(self):
        starting_position = int(self.asset_offset / 2)
        self.transaction.amount = read_bit64(self.serialized, offset=starting_position)
        self.transaction.parse_signatures(
            hexlify(self.serialized).decode(), self.asset_offset + 8 * 2
        )
        return self.transaction
