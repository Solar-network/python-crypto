from solar_crypto.transactions.deserializer import Deserializer


def test_delegate_resignation_temp_deserializer(transaction_type_7_0):
    serialized = transaction_type_7_0["serialized"]  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 3
    assert actual.network == 30
    assert actual.typeGroup == 1
    assert actual.type == 7
    assert actual.nonce == 1
    assert actual.senderPublicKey == transaction_type_7_0["senderPublicKey"]
    # assert actual.asset["resignationType"] == 1
    assert actual.fee == 0
    assert actual.signature == transaction_type_7_0["signature"]
    assert actual.amount == 0


def test_delegate_resignation_perm_deserializer(transaction_type_7_1):
    serialized = transaction_type_7_1["serialized"]  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 3
    assert actual.network == 30
    assert actual.typeGroup == 1
    assert actual.type == 7
    assert actual.nonce == 1
    assert actual.senderPublicKey == transaction_type_7_1["senderPublicKey"]
    assert actual.asset["resignationType"] == 1
    assert actual.fee == 0
    assert actual.signature == transaction_type_7_1["signature"]
    assert actual.amount == 0
