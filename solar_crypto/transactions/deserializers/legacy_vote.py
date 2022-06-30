from binascii import hexlify

from binary.unsigned_integer.reader import read_bit8

from solar_crypto.exceptions import SolarDeserializerException
from solar_crypto.transactions.deserializers.base import BaseDeserializer


class LegacyVoteDeserializer(BaseDeserializer):
    def deserialize(self):
        starting_position = int(self.asset_offset / 2)
        offset = 0

        vote_length = read_bit8(self.serialized, offset=starting_position)
        offset += 1

        self.transaction.asset["votes"] = []

        for _ in range(vote_length):
            if (
                self.transaction.version == 2
                and self.serialized[starting_position + offset : starting_position + offset + 1]
                != b"\xff"
            ):
                vote_buffer = self.serialized[
                    starting_position + offset : starting_position + offset + 34
                ]
                offset += 34
                prefix = "+" if vote_buffer[0] == 1 else "-"
                vote = f"{prefix}{vote_buffer[1::].hex()}"
            else:
                if self.transaction.version == 2:
                    offset += 1  # +1 due to NOT moving forwards when checking for `b"\xff"`

                length = read_bit8(
                    self.serialized[starting_position + offset : starting_position + offset + 1]
                )
                offset += 1

                vote_buffer = self.serialized[
                    starting_position + offset : starting_position + offset + length
                ]
                offset += length

                prefix = "+" if vote_buffer[0] == 1 else "-"
                vote = f"{prefix}{vote_buffer[1::].decode()}"

            if len(vote) <= 1:
                raise SolarDeserializerException("Invalid transaction data")

            self.transaction.asset["votes"].append(vote)

        self.transaction.parse_signatures(
            hexlify(self.serialized).decode(), self.asset_offset + 2 + ((offset - 1) * 2)
        )

        return self.transaction
