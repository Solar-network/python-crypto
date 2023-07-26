from typing import Optional

from solar_crypto.constants import (
    TRANSACTION_DELEGATE_RESIGNATION,
    TRANSACTION_TYPE_GROUP,
    ResignationType,
)

from solar_crypto.transactions.builder.base import BaseTransactionBuilder


class DelegateResignation(BaseTransactionBuilder):

    transaction_type = TRANSACTION_DELEGATE_RESIGNATION

    def __init__(self, resignation_type: ResignationType = None, fee: Optional[int] = None):
        """Create a delegate resignation transaction

        Args:
            resignation_type (int, optional): resignation type (0 - temporary, 1 - permanent, 2 - revoke)
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()

        self.transaction.typeGroup = self.get_type_group()

        self.transaction.asset["resignationType"] = resignation_type

        if fee:
            self.transaction.fee = fee

    def set_resignation_type(self, resignation_type: ResignationType):
        """Set resignation type

        Args:
            resignation_type (ResignationType): resignation type (0 - temporary, 1 - permanent, 2 revoke)
        """
        self.transaction.asset["resignationType"] = resignation_type

    def get_type_group(self) -> int:
        return TRANSACTION_TYPE_GROUP.CORE.value
