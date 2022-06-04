from binascii import hexlify

from binary.unsigned_integer.reader import read_bit8

from solar_crypto.transactions.deserializers.base import BaseDeserializer


class HtlcClaimDeserializer(BaseDeserializer):
    def deserialize(self):
        starting_position = int(self.asset_offset / 2)
        offset = 0

        hash_type = read_bit8(self.serialized, offset=starting_position)
        offset += 1

        lock_transaction_id = hexlify(
            self.serialized[starting_position + offset : starting_position + offset + 32]
        )
        offset += 32

        unlock_secret_length = read_bit8(self.serialized, offset=starting_position + offset)
        offset += 1

        unlock_secret = hexlify(
            self.serialized[
                starting_position + offset : starting_position + offset + unlock_secret_length
            ]
        )
        offset += unlock_secret_length

        self.transaction.asset["claim"] = {
            "hashType": hash_type,
            "lockTransactionId": lock_transaction_id.decode(),
            "unlockSecret": unlock_secret.decode(),
        }

        self.transaction.parse_signatures(
            hexlify(self.serialized).decode(), self.asset_offset + (offset * 2)
        )

        return self.transaction
