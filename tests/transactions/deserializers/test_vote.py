from solar_crypto.transactions.deserializer import Deserializer


def test_vote_deserializer():
    serialized = "ff031e0200000002000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c00e1f50500000000000108646561646c6f636ba9138ee49974901f9818d56459d1817c41fc2d51204abc07cea05b72cae00cffaf314057f06b009ce6a2f99c8774af171f209fac1a9ce15abb429648ea22321765cb"  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()
    assert actual.version == 3
    assert actual.network == 30
    assert actual.typeGroup == 2
    assert actual.type == 2
    assert actual.amount == 0
    assert actual.fee == 100000000
    assert actual.nonce == 1
    assert actual.asset["votes"] == {"deadlock": 50.33}
    assert (
        actual.senderPublicKey
        == "037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c"
    )  # noqa
    assert (
        actual.signature
        == "8ee49974901f9818d56459d1817c41fc2d51204abc07cea05b72cae00cffaf314057f06b009ce6a2f99c8774af171f209fac1a9ce15abb429648ea22321765cb"
    )

    actual.verify()


def test_vote_deserializer_multiple_votes():
    serialized = "ff031e0200000002000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c00e1f5050000000000020366756eca0d08646561646c6f636b46196300f3ff5eff1a2e083ab31762089ad95bebb3de8ee451442a5fd945c2d7773cfe5dfc1528d0c03533677b88cd9e4421395716f78e9f7519343d2fb43ef1ca8d"

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.asset["votes"] == {"fun": 35.3, "deadlock": 64.7}
    assert (
        actual.senderPublicKey
        == "037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c"
    )  # noqa
