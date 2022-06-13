from decimal import Decimal

from binary.unsigned_integer.writer import write_bit8, write_bit16

from solar_crypto.transactions.serializers.base import BaseSerializer


class VoteSerializer(BaseSerializer):
    """Serializer handling vote data"""

    def serialize(self):
        self.bytes_data += write_bit8(len(self.transaction["asset"]["votes"]))

        if len(self.transaction["asset"]["votes"]) == 0:
            return self.bytes_data

        for vote, percent in self.transaction["asset"]["votes"].items():
            self.bytes_data += write_bit8(len(vote))
            self.bytes_data += vote.encode()
            self.bytes_data += write_bit16(int(Decimal(str(percent)) * 100))

        return self.bytes_data
