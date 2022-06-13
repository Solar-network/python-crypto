from binascii import hexlify

from binary.unsigned_integer.reader import read_bit8, read_bit16

from solar_crypto.transactions.deserializers.base import BaseDeserializer


class VoteDeserializer(BaseDeserializer):
    def deserialize(self):
        starting_position = int(self.asset_offset / 2)
        offset = 0

        number_of_votes = read_bit8(self.serialized, offset=starting_position)
        offset += 1

        self.transaction.asset["votes"] = dict()

        for _ in range(number_of_votes):
            vote_len: int = read_bit8(self.serialized, offset=starting_position + offset)
            offset += 1

            vote: str = self.serialized[
                starting_position + offset : starting_position + offset + vote_len
            ].decode()
            offset += vote_len

            percent = read_bit16(self.serialized, offset=starting_position + offset) / 100
            offset += 2

            self.transaction.asset["votes"].update({vote: percent})

        self.transaction.parse_signatures(
            hexlify(self.serialized).decode(), self.asset_offset + 2 + ((offset - 1) * 2)
        )

        return self.transaction
