import typing

from solar_crypto.constants import TRANSACTION_VOTE
from solar_crypto.identity.address import address_from_passphrase
from solar_crypto.transactions.builder.base import BaseTransactionBuilder


class LegacyVote(BaseTransactionBuilder):

    transaction_type = TRANSACTION_VOTE

    def __init__(self, vote=None, fee=None):
        """Legacy vote transaction

        Args:
            vote (str): address of a delegate you want to vote
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()

        self.transaction.asset["votes"] = []
        if vote:
            self.transaction.asset["votes"].append(vote)

        if fee:
            self.transaction.fee = fee

    def set_votes(self, votes: typing.List[str]):
        """Set votes/unvotes

        Args:
            votes (List[str]): list of votes
        """
        self.transaction.asset["votes"] = votes

    def sign(self, passphrase):
        self.transaction.recipientId = address_from_passphrase(passphrase)
        super().sign(passphrase)
