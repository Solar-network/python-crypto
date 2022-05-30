import pytest


@pytest.fixture
def transaction_type_0():
    """Transaction of type "transfer" """
    data = {
        "amount": 200000000,
        "asset": {},
        "fee": 10000000,
        "id": "c868363929575b00d58846c55139143ada15fec07c917d7139b8a422874adaf0",
        "recipientId": "D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib",
        "senderPublicKey": "034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192",
        "signature": "20b4091da824dc1b630ec7a09f39fe491cb2ac39dabdbe67d48753a43e8dc8cd4f76eb4ff717efbb06889882aa99a07db7bf35de3b8d5f1ad74b8284e0a68420",
        "nonce": 1,
        "type": 0,
        "typeGroup": 1,
        "version": 3,
        "serialized": "ff031e0100000000000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19280969800000000000000c2eb0b00000000000000001e0995750207ecaf0ccf251c1265b92ad84f55366220b4091da824dc1b630ec7a09f39fe491cb2ac39dabdbe67d48753a43e8dc8cd4f76eb4ff717efbb06889882aa99a07db7bf35de3b8d5f1ad74b8284e0a68420",
        "network": 30,
    }

    return data


@pytest.fixture
def transaction_type_1():
    """Transaction of type "second signature registration" """
    data = {
        "version": 2,
        "network": 23,
        "typeGroup": 1,
        "type": 1,
        "nonce": 1,
        "senderPublicKey": "034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192",
        "fee": 500000000,
        "asset": {
            "signature": {
                "publicKey": "03699e966b2525f9088a6941d8d94f7869964a000efe65783d78ac82e1199fe609"
            }
        },
        "signature": "f9a1e2244c8318e8be85482fc02659e5c1775d246d73d5d0699ae4a1d5e3a3e84f9dcf68ee015f943d2a82eb829f35abd7901279761d96f6b43431520e955c67",  # noqa
        "amount": 0,
        "id": "173a3230159b45d772b2e0348f42af53913bf3e376397f29b8e0bda290badbe4",
        "serialized": "ff02170100000001000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed1920065cd1d000000000003699e966b2525f9088a6941d8d94f7869964a000efe65783d78ac82e1199fe609f9a1e2244c8318e8be85482fc02659e5c1775d246d73d5d0699ae4a1d5e3a3e84f9dcf68ee015f943d2a82eb829f35abd7901279761d96f6b43431520e955c67",  # noqa
    }
    return data


@pytest.fixture
def transaction_type_2():
    """Transaction of type "delegate registration" """
    data = {
        "version": 2,
        "network": 23,
        "typeGroup": 1,
        "type": 2,
        "nonce": 1,
        "senderPublicKey": "034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192",
        "fee": 2500000000,
        "asset": {"delegate": {"username": "boldninja"}},
        "signature": "eaf4b4dfd7903c32cf6c145ddf0744e86536719f5790b4286b08f1a10f0ad183bc601efc8a49a2a7b41758601a1793693afa1781cf0a63a8f72b08d5a1aaba1e",  # noqa
        "amount": 0,
        "id": "cfd113d8cd9fd46b07030c14fac38c1d3fc0eca991e999eab9d0152ea96ab0dc",
        "serialized": "ff02170100000002000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19200f90295000000000009626f6c646e696e6a61eaf4b4dfd7903c32cf6c145ddf0744e86536719f5790b4286b08f1a10f0ad183bc601efc8a49a2a7b41758601a1793693afa1781cf0a63a8f72b08d5a1aaba1e",  # noqa
    }
    return data


@pytest.fixture
def transaction_type_3():
    """Transaction of type "vote" """
    data = {
        "version": 2,
        "network": 23,
        "typeGroup": 1,
        "type": 3,
        "nonce": 1,
        "senderPublicKey": "034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192",
        "fee": 100000000,
        "asset": {"votes": ["+022cca9529ec97a772156c152a00aad155ee6708243e65c9d211a589cb5d43234d"]},
        "signature": "86007f8e6a982bc271ec063c20f158734f0bc1e23e0e1abf9edeaa208b4810fa1d466171bba79a5c00b0a4c698728f68aa0748d98613cac247c014ee84a6fc41",  # noqa
        "amount": 0,
        "id": "2c5d71028607674411c8e37e316a015eccbeb9ba486fddfbd393dc421540a90a",
        "serialized": "ff02170100000003000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19200e1f50500000000000101022cca9529ec97a772156c152a00aad155ee6708243e65c9d211a589cb5d43234d86007f8e6a982bc271ec063c20f158734f0bc1e23e0e1abf9edeaa208b4810fa1d466171bba79a5c00b0a4c698728f68aa0748d98613cac247c014ee84a6fc41",  # noqa
    }
    return data


@pytest.fixture
def transaction_type_4():
    """Transaction of type "multi signature registration" """
    data = {
        "version": 2,
        "network": 23,
        "typeGroup": 1,
        "type": 4,
        "nonce": 1,
        "senderPublicKey": "0205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b896",
        "id": "c868aad20165a336c35e324378f0c12008d18af4c1025291efcb7539c7c917f0",
        "amount": 0,
        "fee": 2000000000,
        "signature": "f5e9859c955bf8917b308ea21c88daf58661686c2017e476dcf735ad7f00aebf8e6effda3fe99e5f33f6007db7db9c9155796d9b5d31c53bd6156364a6a765d0",  # noqa
        "asset": {
            "multiSignature": {
                "publicKeys": [
                    "0205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b896",
                    "03df0a1eb42d99b5de395cead145ba1ec2ea837be308c7ce3a4e8018b7efc7fdb8",
                    "03860d76b1df09659ac282cea3da5bd84fc45729f348a4a8e5f802186be72dc17f",
                ],
                "min": 2,
            }
        },
        "signatures": [
            "0064900cb2cc3db6ca9c7e3bd363b322cdc4a39e051f655e9867935e1bb856b6dcce52845c031c690808f40340bc827bbaacd7b04bceff866cb0d386ab84715174",  # noqa
            "01dd363ccc101a958bded1a5db1c08f13283fc7cee53da93dfe00785eb406512467ff8e445f8ad843744ac4179f30f942645dfd5bdf5f2bfc344ad02393053880a",  # noqa
            "02d0012f035dc3fd54173c83d40217914653488fe9ce592dca34234163181d255281f2be7033725cfc4a6786509e7fabbaf0be8cf50882fc7b66fe94f259fd004e",  # noqa
        ],
        "serialized": "ff021701000000040001000000000000000205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b89600943577000000000002030205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b89603df0a1eb42d99b5de395cead145ba1ec2ea837be308c7ce3a4e8018b7efc7fdb803860d76b1df09659ac282cea3da5bd84fc45729f348a4a8e5f802186be72dc17ff5e9859c955bf8917b308ea21c88daf58661686c2017e476dcf735ad7f00aebf8e6effda3fe99e5f33f6007db7db9c9155796d9b5d31c53bd6156364a6a765d00064900cb2cc3db6ca9c7e3bd363b322cdc4a39e051f655e9867935e1bb856b6dcce52845c031c690808f40340bc827bbaacd7b04bceff866cb0d386ab8471517401dd363ccc101a958bded1a5db1c08f13283fc7cee53da93dfe00785eb406512467ff8e445f8ad843744ac4179f30f942645dfd5bdf5f2bfc344ad02393053880a02d0012f035dc3fd54173c83d40217914653488fe9ce592dca34234163181d255281f2be7033725cfc4a6786509e7fabbaf0be8cf50882fc7b66fe94f259fd004e",  # noqa
    }
    return data


@pytest.fixture
def transaction_type_5():
    """Transaction of type "ipfs" """
    data = {
        "version": 2,
        "network": 23,
        "typeGroup": 1,
        "type": 5,
        "nonce": 1,
        "senderPublicKey": "034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192",
        "fee": 500000000,
        "amount": 0,
        "asset": {"ipfs": "QmR45FmbVVrixReBwJkhEKde2qwHYaQzGxu4ZoDeswuF9w"},
        "signature": "0b6e81b123de99e953d3073a8760d3213ab5f5cf512e65a2dd73aebb410966d8fbc59e775deb4f23c51be0847402b5e1d4ee68732b3e6d8e8914d259d7e373eb",
        "id": "818228ce634b46c488f3b2df8fd02bd50331ebdedb44df5b9b11b97b01e9fb36",
        "serialized": "ff02170100000005000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed1920065cd1d000000000012202853f0f11ab91d73b73a2a86606103f45dd469ad2e89ec6f9a25febe8758d3fe0b6e81b123de99e953d3073a8760d3213ab5f5cf512e65a2dd73aebb410966d8fbc59e775deb4f23c51be0847402b5e1d4ee68732b3e6d8e8914d259d7e373eb",
    }
    return data


@pytest.fixture
def transaction_type_6():
    """Transaction of type "multi payment" """
    data = {
        "amount": 0,
        "asset": {
            "payments": [
                {"amount": 1, "recipientId": "DEMvpU4Qq6KvSzF3sRNjGCkm6Kj7cFfVaz"},
                {"amount": 2, "recipientId": "DQveGkK7te33dWJwHgKpGKDr5amxAE7PF4"},
            ]
        },
        "fee": 10000000,
        "id": "8f148f2fdda47fde762edb24a37929d59af7906b7c455094266a5ed75dffba50",
        "network": 30,
        "senderPublicKey": "037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c",
        "signature": "4b09083a78f12d54b3b320b5793de8fafca95927ff368a6102e78bca87645efee92ca076c72062727e05f2e5033ad4980251894a696925588ff4a90665a6b231",
        "nonce": 1,
        "type": 6,
        "typeGroup": 1,
        "version": 3,
        "serialized": "ff031e0100000006000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c809698000000000000020001000000000000001e65266cddfeec4b27a292a95d06f3d45bf9f3f61502000000000000001ed90798e15fd33f001b7c6c587dc78ae0c7d67d8c4b09083a78f12d54b3b320b5793de8fafca95927ff368a6102e78bca87645efee92ca076c72062727e05f2e5033ad4980251894a696925588ff4a90665a6b231",
    }
    return data


@pytest.fixture
def transaction_type_7():
    """Transaction of type "delegate resignation" """
    data = {
        "version": 2,
        "network": 23,
        "typeGroup": 1,
        "type": 7,
        "nonce": 1,
        "senderPublicKey": "034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192",
        "fee": 2500000000,
        "amount": 0,
        "signature": "bdc048ca7eb5688cc01921aecf5914118cfc78eacc23825efa6d75094a683127cc02512dc59e1e0631fa8956f482eabc54933d23011a8337ea9cab99abed504d",
        "id": "707b4deb339e717dfef44c40db0692015ce9bbab015c007b016b8a46b341e859",
        "serialized": "ff02170100000007000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19200f902950000000000bdc048ca7eb5688cc01921aecf5914118cfc78eacc23825efa6d75094a683127cc02512dc59e1e0631fa8956f482eabc54933d23011a8337ea9cab99abed504d",
    }
    return data


@pytest.fixture
def transaction_type_8():
    """Transaction of type "HTLC lock" """
    data = {
        "amount": 200000000,
        "asset": {
            "lock": {
                "secretHash": "1691053581dd80959b68ec8941898837790a43ec883bb32a2a9ea10edbb57c24",
                "expiration": {"type": 1, "value": 1573455822},
            }
        },
        "fee": 10000000,
        "id": "61c27654fba0cabdb7ba38ccf2c1dffe136f605572f465d9ec14d5001875ad65",
        "network": 30,
        "recipientId": "D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib",
        "senderPublicKey": "037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c",
        "signature": "d1cbd1784d67802b68c1b0ede92626d20cbb2b6351dea704441311bebd7da325f3e7a0f7305ca4634ea2ccaca627cc86db83006647f2a6f246f075c13ffa3b3f",
        "nonce": 1,
        "type": 8,
        "typeGroup": 1,
        "version": 3,
        "serialized": "ff031e0100000008000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c80969800000000000000c2eb0b00000000201691053581dd80959b68ec8941898837790a43ec883bb32a2a9ea10edbb57c2401ce07c95d1e0995750207ecaf0ccf251c1265b92ad84f553662d1cbd1784d67802b68c1b0ede92626d20cbb2b6351dea704441311bebd7da325f3e7a0f7305ca4634ea2ccaca627cc86db83006647f2a6f246f075c13ffa3b3f",
    }
    return data


@pytest.fixture
def transaction_type_9():
    """Transaction of type "HTLC claim" """
    data = {
        "amount": 0,
        "asset": {
            "claim": {
                "hashType": 0,
                "lockTransactionId": "943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4",
                "unlockSecret": "1e9f2bbccc07c643316be6faae9f004cc16dec3910501387fd326cd8a39b4fdb",
            }
        },
        "fee": 0,
        "senderPublicKey": "037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c",
        "signature": "1b980072eccd0edfa926bc4f20c5e8d94b6a186d5343ab12305662ad66dd33764f6812b8e05474c7cdee3bc00d48fc73a4d6e33fd625276de4c7d754fba9261f",
        "nonce": 1,
        "type": 9,
        "typeGroup": 1,
        "version": 3,
        "serialized": "ff031e0100000009000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c00000000000000000000943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4201e9f2bbccc07c643316be6faae9f004cc16dec3910501387fd326cd8a39b4fdb1b980072eccd0edfa926bc4f20c5e8d94b6a186d5343ab12305662ad66dd33764f6812b8e05474c7cdee3bc00d48fc73a4d6e33fd625276de4c7d754fba9261f",
    }
    return data


@pytest.fixture
def transaction_type_10():
    """Transaction of type "HTLC refund" """
    data = {
        "version": 2,
        "network": 23,
        "typeGroup": 1,
        "type": 10,
        "nonce": 1,
        "senderPublicKey": "034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192",
        "fee": 0,
        "amount": 0,
        "asset": {
            "refund": {
                "lockTransactionId": "943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4",
            },
        },
        "signature": "16d9ef1dceb0cbb105a45af6bdde9439055f07197643f9e2837312463330fd02ec7b13d1242becfe333c1b8ab2ea91c0c8240390d86f0fb0f6cdc22ec6ac64f1",
        "id": "9356aa730990a2ea8e9871ffa65800f34ef1a4bec3215d89c950e72d82a34e91",
        "serialized": "ff0217010000000a000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192000000000000000000943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb416d9ef1dceb0cbb105a45af6bdde9439055f07197643f9e2837312463330fd02ec7b13d1242becfe333c1b8ab2ea91c0c8240390d86f0fb0f6cdc22ec6ac64f1",
    }
    return data


@pytest.fixture
def transaction_type_burn():
    """Transaction of type burn"""
    data = {
        "amount": 2500000,
        "asset": {},
        "fee": 0,
        "id": "7e1dfa5cc0f70155530438d271885d39370fa0143287e8f6d40d2e67b9b6e366",
        "senderPublicKey": "03fe61f79ee50c5f45acfc37b33c3a5c10e2afe0204e3c8fa2a2d3d73a2b412360",
        "signature": "ef071aa1c7631a6ace4227f583c78d922e938a1c3a8997a959e834e6b43ece34313a68dcf56ac606fb387006d9cbc962249376326c9dd84b81979eed5d1163d8",
        "nonce": 1,
        "type": 0,
        "typeGroup": 2,
        "version": 2,
        "network": 30,
        "serialized": "ff021e020000000000010000000000000003fe61f79ee50c5f45acfc37b33c3a5c10e2afe0204e3c8fa2a2d3d73a2b412360000000000000000000a025260000000000ef071aa1c7631a6ace4227f583c78d922e938a1c3a8997a959e834e6b43ece34313a68dcf56ac606fb387006d9cbc962249376326c9dd84b81979eed5d1163d8",
    }
    return data


@pytest.fixture
def message():
    data = {
        "camelCase_pk": {
            "publicKey": "034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192",
            "signature": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798f9ee8f2b718dc55e840f906c5071f63694ddeb35af8858f2a54cfdb3bd36fce1",  # noqa
            "message": "Hello World",
        },
        "snake_case_pk": {
            "publickey": "034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192",
            "signature": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798f9ee8f2b718dc55e840f906c5071f63694ddeb35af8858f2a54cfdb3bd36fce1",  # noqa
            "message": "Hello World",
        },
        "passphrase": "this is a top secret passphrase",
    }
    return data
