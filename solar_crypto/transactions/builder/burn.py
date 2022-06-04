from solar_crypto.constants import SOLAR_TRANSACTION_BURN, TRANSACTION_TYPE_GROUP
from solar_crypto.transactions.builder.base import BaseTransactionBuilder


class Burn(BaseTransactionBuilder):

    transaction_type = SOLAR_TRANSACTION_BURN
    typeGroup = TRANSACTION_TYPE_GROUP.SOLAR.value

    def __init__(self, amount):
        """Create a burn transaction

        Args:
            amount (int): amount of coins you want to burn
        """
        super().__init__()

        if type(amount) == int and amount > 0:
            self.transaction.amount = amount
        else:
            raise ValueError("Amount is not valid")
