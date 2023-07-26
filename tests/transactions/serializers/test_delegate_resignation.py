from solar_crypto.transactions.serializer import Serializer


def test_serializer_0(transaction_type_7_0):
    result = Serializer(transaction_type_7_0).serialize(False, True)
    assert result == transaction_type_7_0["serialized"]


def test_serializer_1(transaction_type_7_1):
    result = Serializer(transaction_type_7_1).serialize(False, True)
    assert result == transaction_type_7_1["serialized"]
