from binascii import hexlify

from base58 import b58decode_check
from binary.hex.writer import write_high
from binary.unsigned_integer.writer import write_bit16, write_bit64

from solar_crypto.exceptions import SolarSerializerException
from solar_crypto.identity import address
from solar_crypto.transactions.serializers.base import BaseSerializer


class TransferSerializer(BaseSerializer):
    """Serializer handling transfer data"""

    def serialize(self):
        self.bytes_data += write_bit16(len(self.transaction["asset"]["transfers"]))

        for transfer in self.transaction["asset"]["transfers"]:
            if not address.validate_address(transfer["recipientId"]):
                raise SolarSerializerException("Invalid recipient address")

            self.bytes_data += write_bit64(transfer["amount"])
            recipientId = hexlify(b58decode_check(transfer["recipientId"]))
            self.bytes_data += write_high(recipientId)

        return self.bytes_data
