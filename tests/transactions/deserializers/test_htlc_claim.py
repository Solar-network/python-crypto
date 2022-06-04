from solar_crypto.constants import HashingType
from solar_crypto.transactions.deserializer import Deserializer


def test_htlc_claim_deserializer():
    serialized = "ff031e0100000009000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c00000000000000000000943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4201e9f2bbccc07c643316be6faae9f004cc16dec3910501387fd326cd8a39b4fdb1b980072eccd0edfa926bc4f20c5e8d94b6a186d5343ab12305662ad66dd33764f6812b8e05474c7cdee3bc00d48fc73a4d6e33fd625276de4c7d754fba9261f"  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 3
    assert actual.network == 30
    assert actual.typeGroup == 1
    assert actual.type == 9
    assert actual.nonce == 1
    assert (
        actual.senderPublicKey
        == "037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c"
    )
    assert actual.fee == 0
    assert actual.amount == 0
    assert (
        actual.asset["claim"]["lockTransactionId"]
        == "943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4"
    )  # noqa
    assert actual.asset["claim"]["hashType"] == HashingType.SHA256.value
    assert (
        actual.asset["claim"]["unlockSecret"]
        == "1e9f2bbccc07c643316be6faae9f004cc16dec3910501387fd326cd8a39b4fdb"
    )  # noqa
    assert (
        actual.signature
        == "1b980072eccd0edfa926bc4f20c5e8d94b6a186d5343ab12305662ad66dd33764f6812b8e05474c7cdee3bc00d48fc73a4d6e33fd625276de4c7d754fba9261f"
    )

    actual.verify()
