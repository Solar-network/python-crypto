from binascii import hexlify

from base58 import b58decode_check
from binary.hex.writer import write_high
from binary.unsigned_integer.writer import write_bit32, write_bit64

from solar_crypto.exceptions import SolarSerializerException
from solar_crypto.identity import address
from solar_crypto.transactions.serializers.base import BaseSerializer


class LegacyTransferSerializer(BaseSerializer):
    """Serializer handling transfer data"""

    def serialize(self):
        if not address.validate_address(self.transaction["recipientId"]):
            raise SolarSerializerException("Invalid recipient address")

        self.bytes_data += write_bit64(self.transaction["amount"])
        self.bytes_data += write_bit32(self.transaction.get("expiration", 0))
        recipientId = hexlify(b58decode_check(self.transaction["recipientId"]))
        self.bytes_data += write_high(recipientId)

        return self.bytes_data
