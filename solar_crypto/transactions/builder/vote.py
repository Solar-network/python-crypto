import re
import typing
from functools import cmp_to_key
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


def cmp(a: typing.List[typing.Union[int, str]], b: typing.List[typing.Union[int, str]]):
    """
    Compare two alphanum keys
    """
    return (a > b) - (a < b)


def nat_cmp(a: str, b: str):
    """
    Natural comparison
    """
    convert = lambda text: int(text) if text.isdigit() else text.lower()  # noqa: E731
    alphanum_key = lambda key: [convert(c) for c in re.split("([0-9]+)", key)]  # noqa: E731
    return cmp(alphanum_key(a), alphanum_key(b))


def sorter(
    a: typing.Tuple[str, typing.Union[float, int]], b: typing.Tuple[str, typing.Union[float, int]]
):
    """
    Sort using desc weight and asc by name
    """
    if b[1] > a[1]:
        return 1
    elif b[1] < a[1]:
        return -1
    else:
        return nat_cmp(a[0], b[0])


def sort_votes(votes: typing.Dict[str, typing.Union[float, int]]):
    """
    Sort votes using custom sorter function
    """
    sorter_fn = cmp_to_key(sorter)
    sorted_votes = sorted(votes.items(), key=sorter_fn)
    return dict(sorted_votes)
