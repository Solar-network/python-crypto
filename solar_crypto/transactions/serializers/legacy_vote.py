from binascii import hexlify, unhexlify

from binary.unsigned_integer.writer import write_bit8

from solar_crypto.transactions.serializers.base import BaseSerializer


class LegacyVoteSerializer(BaseSerializer):
    """Serializer handling legacy vote"""

    def serialize(self):
        vote_bytes = []

        for vote in self.transaction["asset"]["votes"]:
            prefix = "01" if vote.startswith("+") else "00"
            sliced = vote[1::]

            if len(sliced) == 66:
                vote_bytes.append(f"{prefix}{sliced}")
                continue

            # vote.length.toString(16).padStart(2, "0") + prefix + Buffer.from(sliced).toString("hex");
            start = format(len(vote), "x").zfill(2)
            vote_hex = f"{start}{prefix}{hexlify(sliced.encode()).decode()}"
            if self.transaction["version"] == 2:
                vote_hex = f"ff{vote_hex}"

            vote_bytes.append(vote_hex)

        self.bytes_data += write_bit8(len(self.transaction["asset"]["votes"]))
        self.bytes_data += unhexlify("".join(vote_bytes))

        return self.bytes_data
