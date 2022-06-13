from solar_crypto.transactions.serializer import Serializer


def test_serializer(transaction_type_legacy_vote):
    result = Serializer(transaction_type_legacy_vote).serialize(False, True)
    assert result == transaction_type_legacy_vote["serialized"]
