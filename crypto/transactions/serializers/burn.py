from binary.unsigned_integer.writer import write_bit64


from crypto.transactions.serializers.base import BaseSerializer


class BurnSerializer(BaseSerializer):
    """Serializer handling timelock refund data
    """

    def serialize(self):
        self.bytes_data += write_bit64(self.transaction['amount'])
        return self.bytes_data
