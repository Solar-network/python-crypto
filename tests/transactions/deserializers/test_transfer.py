from solar_crypto.transactions.deserializer import Deserializer


def test_deserializer(transaction_type_6):
    serialized = transaction_type_6["serialized"]

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 3
    assert actual.network == 30
    assert actual.typeGroup == 1
    assert actual.type == 6
    assert actual.nonce == 1
    assert (
        actual.senderPublicKey
        == "037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c"
    )
    assert actual.fee == 10000000
    assert (
        actual.signature
        == "4b09083a78f12d54b3b320b5793de8fafca95927ff368a6102e78bca87645efee92ca076c72062727e05f2e5033ad4980251894a696925588ff4a90665a6b231"
    )
    assert actual.amount == 0
    assert actual.asset["transfers"][0]["amount"] == 1  # noqa
    assert (
        actual.asset["transfers"][0]["recipientId"] == "DEMvpU4Qq6KvSzF3sRNjGCkm6Kj7cFfVaz"
    )  # noqa
    assert actual.asset["transfers"][1]["amount"] == 2  # noqa
    assert (
        actual.asset["transfers"][1]["recipientId"] == "DQveGkK7te33dWJwHgKpGKDr5amxAE7PF4"
    )  # noqa

    actual.verify()


def test_deserializer_two_fifty_six_transfers(transaction_type_6_256):
    serialized = transaction_type_6_256["serialized"]
    deserializer = Deserializer(serialized)
    transaction_dict = deserializer.deserialize().to_dict()

    assert len(transaction_dict["asset"]["transfers"]) == 256
