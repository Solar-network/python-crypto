from binary.unsigned_integer.reader import read_bit8

from solar_crypto.transactions.deserializers.base import BaseDeserializer


class DelegateResignationDeserializer(BaseDeserializer):
    def deserialize(self):
        starting_position = int(self.asset_offset / 2)
        remainder_len = len(self.serialized) - starting_position
        offset = 0

        if (remainder_len <= 128 and remainder_len % 64 == 0) or (
            remainder_len >= 130 and remainder_len % 65 == 0
        ):
            # do nothing, continue as usual
            pass
        else:
            resignation_type = read_bit8(self.serialized, offset=starting_position)
            offset += 1

            # make sure this is not a signatures array with only one signature since that can be in the range 00-0F here
            if resignation_type <= 0x0F:
                offset -= 1

            self.transaction.asset["resignationType"] = 0xFF - resignation_type

        self.transaction.parse_signatures(self.serialized.hex(), self.asset_offset + (offset * 2))

        return self.transaction
