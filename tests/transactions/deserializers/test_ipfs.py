from crypto.transactions.deserializer import Deserializer


def test_ipfs_deserializer_v2():
    serialized = "ff021e0100000005000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c0065cd1d00000000001220b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde91c553734d23d2c41d6be3ed07d7644730a94be98a3e8301798b6449da9394a2f971b10fcddd09ba34d9d900ac5b093f49431242ee4006aced50da56c994f02b9"  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 2
    assert actual.network == 30
    assert actual.typeGroup == 1
    assert actual.type == 5
    assert actual.nonce == 1
    assert (
        actual.senderPublicKey
        == "037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c"
    )
    assert actual.fee == 500000000
    assert (
        actual.signature
        == "1c553734d23d2c41d6be3ed07d7644730a94be98a3e8301798b6449da9394a2f971b10fcddd09ba34d9d900ac5b093f49431242ee4006aced50da56c994f02b9"
    )
    assert actual.amount == 0
    assert actual.asset["ipfs"] == "QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4"  # noqa

    actual.verify()


def test_ipfs_deserializer_v3():
    serialized = "ff031e0100000005000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c0065cd1d00000000001220b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde990d6b66d19a21ba90b2a7bb400835e511f9037f60ecbc94ed2623876807ee6e64383cc7efdd6927ad4db91cce7d0ca81b0d29ff5babf1be311167a332b456239"  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 3
    assert actual.network == 30
    assert actual.typeGroup == 1
    assert actual.type == 5
    assert actual.nonce == 1
    assert (
        actual.senderPublicKey
        == "037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c"
    )
    assert actual.fee == 500000000
    assert (
        actual.signature
        == "90d6b66d19a21ba90b2a7bb400835e511f9037f60ecbc94ed2623876807ee6e64383cc7efdd6927ad4db91cce7d0ca81b0d29ff5babf1be311167a332b456239"
    )
    assert actual.amount == 0
    assert actual.asset["ipfs"] == "QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4"  # noqa

    actual.verify()
