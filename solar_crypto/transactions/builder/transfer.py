from solar_crypto.constants import TRANSACTION_TYPE_GROUP, TRANSACTION_TRANSFER
from solar_crypto.identity import address
from solar_crypto.transactions.builder.base import BaseTransactionBuilder


class Transfer(BaseTransactionBuilder):

    transaction_type = TRANSACTION_TRANSFER

    def __init__(self, vendorField=None, fee=None):
        """Create a multi payment transaction

        Args:
            vendorField (str): value for the vendor field aka smartbridge
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()

        self.transaction.typeGroup = self.get_type_group()

        self.transaction.asset["transfers"] = []

        self.transaction.vendorField = vendorField.encode() if vendorField else None

        if fee:
            self.transaction.fee = fee

    def get_type_group(self):
        return TRANSACTION_TYPE_GROUP.CORE.value

    def add_payment(self, amount, recipient_id):
        """Legacy method that is deprecated"""
        self.add_transfer(amount, recipient_id)

    def add_transfer(self, amount, recipient_id):
        if not address.validate_address(recipient_id):
            raise ValueError("Invalid recipient address")

        self.transaction.asset["transfers"].append({"amount": amount, "recipientId": recipient_id})
