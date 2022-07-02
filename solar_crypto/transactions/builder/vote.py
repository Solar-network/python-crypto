import re
import typing
from decimal import Decimal
from functools import cmp_to_key
from math import trunc

from solar_crypto.constants import SOLAR_TRANSACTION_VOTE, TRANSACTION_TYPE_GROUP
from solar_crypto.exceptions import SolarInvalidTransaction
from solar_crypto.transactions.builder.base import BaseTransactionBuilder


class Vote(BaseTransactionBuilder):

    transaction_type = SOLAR_TRANSACTION_VOTE
    typeGroup = TRANSACTION_TYPE_GROUP.SOLAR.value

    def __init__(self):
        super().__init__()

        self.transaction.asset["votes"] = []

    def set_votes(
        self,
        votes: typing.Union[
            typing.List[str], typing.Dict[str, typing.Union[int, float, Decimal]]
        ] = dict,
    ):
        """Set votes

        Args:
            votes
        """
        vote_object: typing.Dict[str, typing.Union[float, int]] = {}

        if isinstance(votes, list):
            vote_list = filter(lambda vote: not vote.startswith("-"), votes)
            vote_list = list(
                map(lambda vote: vote[1:] if vote.startswith("+") else vote, vote_list)
            )

            if len(vote_list) > 53:
                raise SolarInvalidTransaction("Unable to vote for more than 53 delegates")

            if len(vote_list) == 0:
                self.transaction.asset["votes"] = {}
                return

            weight = trunc(10000 / len(vote_list))
            remainder = 10000

            for vote in vote_list:
                vote_object[vote] = weight / 100
                remainder -= weight

            for index in range(int(remainder)):
                key = list(vote_object.keys())[index]
                vote_object[key] = round((vote_object[key] + 0.01) * 100) / 100

            votes = vote_object
        else:
            for key, val in votes.items():
                votes[key] = val

        validate(votes)

        if votes:
            nr_of_votes = len(votes.keys())
            if nr_of_votes > 0:
                votes = sort_votes(votes)

        self.transaction.asset["votes"] = votes


def validate(votes):
    for value in votes.values():
        if not valid_precision(value):
            raise SolarInvalidTransaction("Only two decimal places are allowed.")

    if Decimal(sum(votes.values())) != Decimal("100"):
        raise SolarInvalidTransaction("Total vote weight must equal 100.")


def valid_precision(value, max_precision=2):
    if isinstance(value, Decimal):
        if abs(value.as_tuple().exponent) <= max_precision:
            return True
    elif isinstance(value, float) or isinstance(value, str) or isinstance(value, int):
        if str(value)[::-1].find(".") <= max_precision:
            return True
    return False


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
