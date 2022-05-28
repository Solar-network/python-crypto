import pytest

from crypto.exceptions import SolarDeserializerException
from crypto.transactions.deserializer import Deserializer


def test_vote_deserializer_v2_pubkey():
    serialized = "ff021e0100000003000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c00e1f50500000000000101034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed1922db8490f3ba58d38b2180afdf54ab4f73d16a7ef41fba4e2f6b530b906372ae03a9c79f1e632297f4efd66f79128396cecfaff808a6c8316495b46342a3e4e71"  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 2
    assert actual.network == 30
    assert actual.typeGroup == 1
    assert actual.type == 3
    assert actual.amount == 0
    assert actual.fee == 100000000
    assert actual.nonce == 1
    assert actual.asset["votes"] == [
        "+034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192"
    ]  # noqa
    assert (
        actual.senderPublicKey
        == "037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c"
    )  # noqa
    assert (
        actual.signature
        == "2db8490f3ba58d38b2180afdf54ab4f73d16a7ef41fba4e2f6b530b906372ae03a9c79f1e632297f4efd66f79128396cecfaff808a6c8316495b46342a3e4e71"
    )

    actual.verify()


def test_vote_deserializer_v2_username():
    serialized = "ff021e0100000003000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c00e1f505000000000001ff080161737465726978a8782e26dfc5472b450a622f8680e1ab74885af22276a127a98bc6b32124f888acb570fae0c4fc7b76ac398b1acacf5c544b5792df7162a873123a563273f9da"  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 2
    assert actual.network == 30
    assert actual.typeGroup == 1
    assert actual.type == 3
    assert actual.amount == 0
    assert actual.fee == 100000000
    assert actual.nonce == 1
    assert actual.asset["votes"] == ["+asterix"]  # noqa
    assert (
        actual.senderPublicKey
        == "037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c"
    )  # noqa
    assert (
        actual.signature
        == "a8782e26dfc5472b450a622f8680e1ab74885af22276a127a98bc6b32124f888acb570fae0c4fc7b76ac398b1acacf5c544b5792df7162a873123a563273f9da"
    )

    actual.verify()


def test_vote_deserializer_v3_pubkey():
    serialized = "ff031e0100000003000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c00e1f50500000000000101034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192e396e7fab6d43a3cee9632220156a3293de88a33240e61052eaa73516f160644952436a52a8e625b5d1c2b68635473608f3aaf0ba84849af63a1ac2d544e24a2"  # noqa

    deserializer = Deserializer(serialized)
    with pytest.raises(SolarDeserializerException):
        deserializer.deserialize()


def test_vote_deserializer_v3_username():
    serialized = "ff031e0100000003000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c00e1f50500000000000108016173746572697852dc67b7000700902e719ebb6cda3d078e184bd3f85493867042ac368a2e908f837d8a0ae4480f8889c88265681c9cf52843ccccd61521174dcb7abe8365349e"  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 3
    assert actual.network == 30
    assert actual.typeGroup == 1
    assert actual.type == 3
    assert actual.amount == 0
    assert actual.fee == 100000000
    assert actual.nonce == 1
    assert actual.asset["votes"] == ["+asterix"]  # noqa
    assert (
        actual.senderPublicKey
        == "037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c"
    )  # noqa
    assert (
        actual.signature
        == "52dc67b7000700902e719ebb6cda3d078e184bd3f85493867042ac368a2e908f837d8a0ae4480f8889c88265681c9cf52843ccccd61521174dcb7abe8365349e"
    )

    actual.verify()


def test_vote_switch_deserializer_v2_username():
    serialized = "ff021e0100000003000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c00e1f505000000000002ff07006f62656c6978ff0801617374657269784b2e8c9ffe86e8c8e35f1089a6cfce2f2b06622689c5aadf37707485b8e506c6999cc1a390cc0420814e18e5e96fd47fb1c5d92712f5823ac6948b4db6f9d703"  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 2
    assert actual.network == 30
    assert actual.typeGroup == 1
    assert actual.type == 3
    assert actual.amount == 0
    assert actual.fee == 100000000
    assert actual.nonce == 1
    assert actual.asset["votes"] == ["-obelix", "+asterix"]  # noqa
    assert (
        actual.senderPublicKey
        == "037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c"
    )  # noqa
    assert (
        actual.signature
        == "4b2e8c9ffe86e8c8e35f1089a6cfce2f2b06622689c5aadf37707485b8e506c6999cc1a390cc0420814e18e5e96fd47fb1c5d92712f5823ac6948b4db6f9d703"
    )

    actual.verify()


def test_vote_switch_deserializer_v3_username():
    serialized = "ff031e0100000003000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c00e1f50500000000000207006f62656c6978080161737465726978e122a19b73142b4d8453b5107586d11e9d9c4a648dee13de26ea6fe9c7f2d913e91150c55ecc49ad2b78dfbae4adb0cbb7dfee86d7f839127f4d96952315ec79"  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 3
    assert actual.network == 30
    assert actual.typeGroup == 1
    assert actual.type == 3
    assert actual.amount == 0
    assert actual.fee == 100000000
    assert actual.nonce == 1
    assert actual.asset["votes"] == ["-obelix", "+asterix"]  # noqa
    assert (
        actual.senderPublicKey
        == "037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c"
    )  # noqa
    assert (
        actual.signature
        == "e122a19b73142b4d8453b5107586d11e9d9c4a648dee13de26ea6fe9c7f2d913e91150c55ecc49ad2b78dfbae4adb0cbb7dfee86d7f839127f4d96952315ec79"
    )

    actual.verify()
