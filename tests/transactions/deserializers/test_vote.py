from solar_crypto.transactions.deserializer import Deserializer


def test_vote_deserializer():
    serialized = "ff031e0200000002000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c4054890000000000000208646561646c6f636b46190366756eca0db1b484cb3b781b0af8f82f8639c52f25f637100d8adadcdde380c07924ada1cc1c1f5b6107cce1ff86b87ab66806ca1a8ae716e3555198cc7fa324a70f697b54"  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()
    assert actual.version == 3
    assert actual.network == 30
    assert actual.typeGroup == 2
    assert actual.type == 2
    assert actual.amount == 0
    assert actual.fee == 9000000
    assert actual.nonce == 1
    assert actual.asset["votes"] == {"deadlock": 64.7, "fun": 35.3}
    assert (
        actual.senderPublicKey
        == "037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c"
    )  # noqa
    assert (
        actual.signature
        == "b1b484cb3b781b0af8f82f8639c52f25f637100d8adadcdde380c07924ada1cc1c1f5b6107cce1ff86b87ab66806ca1a8ae716e3555198cc7fa324a70f697b54"
    )

    actual.verify()
