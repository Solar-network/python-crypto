from crypto.transactions.serializer import Serializer


def test_serializer(transaction_type_burn):
    result = Serializer(transaction_type_burn).serialize(False, True, True)
    assert result == transaction_type_burn['serialized']
