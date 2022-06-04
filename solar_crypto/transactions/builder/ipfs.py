from solar_crypto.constants import TRANSACTION_IPFS, TRANSACTION_TYPE_GROUP
from solar_crypto.transactions.builder.base import BaseTransactionBuilder


class IPFS(BaseTransactionBuilder):

    transaction_type = TRANSACTION_IPFS

    def __init__(self, ipfs_cid=None, fee=None):
        """Create an ipfs transaction

        Args:
            ipfs_cid (str): ipfs cid
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()

        self.transaction.asset["ipfs"] = ipfs_cid
        self.transaction.typeGroup = self.get_type_group()

        if fee:
            self.transaction.fee = fee

    def get_type_group(self):
        return TRANSACTION_TYPE_GROUP.CORE.value

    def set_ipfs_cid(self, cid: str):
        self.transaction.asset["ipfs"] = cid
