from solar_crypto.transactions.deserializer import Deserializer


def test_htlc_lock_deserializer():
    serialized = "ff031e0100000008000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c80969800000000000000c2eb0b00000000201691053581dd80959b68ec8941898837790a43ec883bb32a2a9ea10edbb57c2401ce07c95d1e0995750207ecaf0ccf251c1265b92ad84f553662d9377c6ff4e9b6b945b2c39606c8cac883d48b259fa5a3688363c8aef75bb0a8f2297249ff835bbf5d6bb3ec66520d3ff99393314258bb498971fbf925bc6b80"

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 3
    assert actual.network == 30
    assert actual.typeGroup == 1
    assert actual.type == 8
    assert actual.nonce == 1
    assert (
        actual.senderPublicKey
        == "037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c"
    )
    assert actual.fee == 10000000
    assert (
        actual.signature
        == "d9377c6ff4e9b6b945b2c39606c8cac883d48b259fa5a3688363c8aef75bb0a8f2297249ff835bbf5d6bb3ec66520d3ff99393314258bb498971fbf925bc6b80"
    )
    assert actual.amount == 200000000
    assert actual.recipientId == "D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib"
    assert (
        actual.asset["lock"]["secretHash"]
        == "1691053581dd80959b68ec8941898837790a43ec883bb32a2a9ea10edbb57c24"
    )  # noqa
    assert actual.asset["lock"]["expiration"]["type"] == 1  # noqa
    assert actual.asset["lock"]["expiration"]["value"] == 1573455822  # noqa

    actual.verify()
