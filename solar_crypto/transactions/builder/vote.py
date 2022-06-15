import typing
from math import trunc

from solar_crypto.constants import SOLAR_TRANSACTION_VOTE, TRANSACTION_TYPE_GROUP
from solar_crypto.transactions.builder.base import BaseTransactionBuilder


class Vote(BaseTransactionBuilder):

    transaction_type = SOLAR_TRANSACTION_VOTE
    typeGroup = TRANSACTION_TYPE_GROUP.SOLAR.value

    def __init__(self):
        super().__init__()

        self.transaction.asset["votes"] = []

    def set_votes(
        self,
        votes: typing.Union[typing.List[str], typing.Dict[str, typing.Union[int, float]]] = dict,
    ):
        """Set votes

        Args:
            votes
        """
        vote_object: typing.Dict[str, typing.Union[float, int]] = {}

        if isinstance(votes, list):
            vote_list = filter(lambda vote: not vote.startswith("-"), votes)
            vote_list = list(map(lambda vote: vote[1:], vote_list))

            if len(vote_list) == 0:
                self.transaction.asset["votes"] = {}
                return

            weight = round((trunc((100 / len(vote_list)) * 100) / 100) * 100)
            remainder = 10000

            for vote in vote_list:
                vote_object[vote] = weight / 100
                remainder -= weight

            for index in range(remainder):
                key = list(vote_object.keys())[index]
                vote_object[key] = round((vote_object[key] + 0.01) * 100) / 100

            votes = vote_object

        if votes:
            nr_of_votes = len(votes.keys())
            if nr_of_votes > 0:
                votes = sort_votes(votes)

        self.transaction.asset["votes"] = votes


def sort_votes(votes: typing.Dict[str, typing.Union[float, int]]):
    sorted_votes = sorted(votes.items(), key=lambda vote: vote[0], reverse=True)
    sorted_votes = sorted(votes.items(), key=lambda vote: vote[1], reverse=True)
    return dict(sorted_votes)
