from binary.unsigned_integer.writer import write_bit8

from solar_crypto.constants import ResignationType
from solar_crypto.exceptions import SolarSerializerException
from solar_crypto.transactions.serializers.base import BaseSerializer


class DelegateResignationSerializer(BaseSerializer):
    """Serializer handling delegate resignation data"""

    def serialize(self):
        resignation_type = self.transaction["asset"].get("resignationType")
        if resignation_type is None:
            raise SolarSerializerException("Resignation type must be set.")

        if not ResignationType._value2member_map_.get(resignation_type):
            raise SolarSerializerException(f"{resignation_type} is not a valid resignation type.")

        if resignation_type == 0:
            return self.bytes_data

        self.bytes_data += write_bit8(0xFF - resignation_type)

        return self.bytes_data
