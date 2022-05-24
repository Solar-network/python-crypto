from crypto.transactions.deserializer import Deserializer


def test_vote_deserializer(transaction_type_burn):
    serialized = transaction_type_burn['serialized']

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 2
    assert actual.network == 30
    assert actual.typeGroup == 2
    assert actual.type == 0
    assert actual.amount == 2500000
    assert actual.fee == 0
    assert actual.nonce == 1
    assert actual.senderPublicKey == '03fe61f79ee50c5f45acfc37b33c3a5c10e2afe0204e3c8fa2a2d3d73a2b412360'  # noqa
    assert actual.id == '7e1dfa5cc0f70155530438d271885d39370fa0143287e8f6d40d2e67b9b6e366'
    assert actual.signature == 'ef071aa1c7631a6ace4227f583c78d922e938a1c3a8997a959e834e6b43ece34313a68dcf56ac606fb387006d9cbc962249376326c9dd84b81979eed5d1163d8'

    actual.verify()
