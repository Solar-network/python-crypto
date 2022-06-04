from binascii import unhexlify

from binary.unsigned_integer.writer import write_bit8

from solar_crypto.transactions.serializers.base import BaseSerializer


class HtlcClaimSerializer(BaseSerializer):
    """Serializer handling timelock claim data"""

    def serialize(self):
        unlock_secret = unhexlify(self.transaction["asset"]["claim"]["unlockSecret"].encode())
        self.bytes_data += write_bit8(self.transaction["asset"]["claim"]["hashType"])
        self.bytes_data += unhexlify(self.transaction["asset"]["claim"]["lockTransactionId"])
        self.bytes_data += write_bit8(len(unlock_secret))
        self.bytes_data += unlock_secret
        return self.bytes_data
