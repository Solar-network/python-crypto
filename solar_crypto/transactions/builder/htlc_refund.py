from typing import Optional

from solar_crypto.constants import TRANSACTION_HTLC_REFUND, TRANSACTION_TYPE_GROUP
from solar_crypto.transactions.builder.base import BaseTransactionBuilder


class HtlcRefund(BaseTransactionBuilder):

    transaction_type = TRANSACTION_HTLC_REFUND

    def __init__(self, lock_transaction_id: str, fee: Optional[int] = None):
        """Create a HTLC refund transaction

        Args:
            lock_transaction_id (str) : HTLC lock transaction ID we wish to claim
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()

        self.transaction.typeGroup = self.get_type_group()

        self.transaction.asset["refund"] = {
            "lockTransactionId": lock_transaction_id,
        }

        if fee:
            self.transaction.fee = fee

    def get_type_group(self) -> int:
        return TRANSACTION_TYPE_GROUP.CORE.value
