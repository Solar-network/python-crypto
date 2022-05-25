from crypto.transactions.deserializer import Deserializer


def test_vote_deserializer():
    serialized = 'ff031e0100000003000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c00e1f50500000000000101034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192fc095c30fba364d579b87ed242e0f886cca53a5c43765a941b237eed2f306d0462a371cfce362d14f5f2ec342806a27480e1c6f60a86887268a146f0b804665a'  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 3
    assert actual.network == 30
    assert actual.typeGroup == 1
    assert actual.type == 3
    assert actual.amount == 0
    assert actual.fee == 100000000
    assert actual.nonce == 1
    assert actual.senderPublicKey == '037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c'  # noqa
    assert actual.id == '7223531535408b2d30ec396a66e56d27a74de829b31484763b74de799c212e79'
    assert actual.signature == 'fc095c30fba364d579b87ed242e0f886cca53a5c43765a941b237eed2f306d0462a371cfce362d14f5f2ec342806a27480e1c6f60a86887268a146f0b804665a'

    assert actual.asset['votes'] == ['+034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192']  # noqa

    actual.verify()


def test_vote_with_vendor_field():
    serialized = 'ff031e0100000003000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c00e1f505000000000b68656c6c6f20776f726c640101034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed1928cfd3bca4512e10680be1ed4ea150773976b04797fb03792fe792f8f046da866dac7d6361e5e39bf6d88bd1cccddbaef1d4b4d2dbb38381ce4a58fa35e16b5cb'  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 3
    assert actual.network == 30
    assert actual.typeGroup == 1
    assert actual.type == 3
    assert actual.amount == 0
    assert actual.fee == 100000000
    assert actual.vendorField == "hello world"
    assert actual.nonce == 1
    assert actual.senderPublicKey == '037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c'  # noqa
    assert actual.id == 'c751be6c2b9525fb1b089b06c942d581a854422eb1fa9567d728c0d00b0b9e6a'
    assert actual.signature == '8cfd3bca4512e10680be1ed4ea150773976b04797fb03792fe792f8f046da866dac7d6361e5e39bf6d88bd1cccddbaef1d4b4d2dbb38381ce4a58fa35e16b5cb'

    assert actual.asset['votes'] == ['+034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192']  # noqa

    actual.verify()
