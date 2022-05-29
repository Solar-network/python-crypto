from crypto.transactions.deserializer import Deserializer


def test_htlc_lock_deserializer(transaction_type_8):
    serialized = transaction_type_8["serialized"]

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 3
    assert actual.network == 30
    assert actual.typeGroup == 1
    assert actual.type == 8
    assert actual.nonce == 1
    assert (
        actual.senderPublicKey
        == "0201cd64fbf55b9de92471c9eb123eeedd9850ebed8fa6703df3af7a6b38631a2f"
    )
    assert actual.fee == 10000000
    assert (
        actual.signature
        == "6a35d659c7965d009254847cebf0d7b34a652a7e8599443e72ba414dd056864b95d05b55d0834dd859a0b1cc3eeee916b7938273fc2984bf9f813c5cf03a93f9"
    )
    assert actual.amount == 200000000
    assert actual.recipientId == "DEMvpU4Qq6KvSzF3sRNjGCkm6Kj7cFfVaz"
    assert (
        actual.asset["lock"]["secretHash"]
        == "1691053581dd80959b68ec8941898837790a43ec883bb32a2a9ea10edbb57c24"
    )  # noqa
    assert actual.asset["lock"]["expiration"]["type"] == 1  # noqa
    assert actual.asset["lock"]["expiration"]["value"] == 1573455822  # noqa

    actual.verify()
