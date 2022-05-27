from binascii import hexlify
from io import BytesIO

from binary.unsigned_integer.reader import read_bit8

from crypto.exceptions import SolarDeserializerException
from crypto.transactions.deserializers.base import BaseDeserializer


class VoteDeserializer(BaseDeserializer):
    def deserialize(self):
        starting_position = int(self.asset_offset / 2)

        buffer = BytesIO(self.serialized[starting_position::])
        vote_length = read_bit8(buffer.read(1))

        self.transaction.asset["votes"] = []
        vote_offset = 0

        for _ in range(vote_length):
            if self.transaction.version == 2 and buffer.read(1) != b"\xff":
                buffer.seek(1)
                vote_offset += 34
                vote_buffer = buffer.read(34)
                prefix = "+" if vote_buffer[0] == 1 else "-"
                vote = f"{prefix}{vote_buffer[1::].hex()}"
            else:
                if self.transaction.version == 2:
                    length = read_bit8(buffer.read(1))
                    vote_buffer = buffer.read(length)
                    vote_offset += length + 2
                else:
                    length = read_bit8(buffer.read(1))
                    vote_buffer = buffer.read(length)
                    vote_offset += length + 1

                prefix = "+" if vote_buffer[0] == 1 else "-"
                vote = f"{prefix}{vote_buffer[1::].decode()}"

            if len(vote) <= 1:
                raise SolarDeserializerException("Invalid transaction data")

            self.transaction.asset["votes"].append(vote)

        self.transaction.parse_signatures(
            hexlify(self.serialized).decode(), self.asset_offset + 2 + (vote_offset * 2)
        )

        return self.transaction
