import pytest


@pytest.fixture
def transaction_type_0():
    """Transaction of type "transfer"
    """
    data = {
        'amount': 200000000,
        'asset': {},
        'fee': 10000000,
        'id': 'c868363929575b00d58846c55139143ada15fec07c917d7139b8a422874adaf0',
        'recipientId': 'D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib',
        'senderPublicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
        'signature': '20b4091da824dc1b630ec7a09f39fe491cb2ac39dabdbe67d48753a43e8dc8cd4f76eb4ff717efbb06889882aa99a07db7bf35de3b8d5f1ad74b8284e0a68420',
        'nonce': 1,
        'type': 0,
        'typeGroup': 1,
        'version': 3,
        'serialized': 'ff031e0100000000000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19280969800000000000000c2eb0b00000000000000001e0995750207ecaf0ccf251c1265b92ad84f55366220b4091da824dc1b630ec7a09f39fe491cb2ac39dabdbe67d48753a43e8dc8cd4f76eb4ff717efbb06889882aa99a07db7bf35de3b8d5f1ad74b8284e0a68420',
        'network': 30,
    }

    return data


@pytest.fixture
def transaction_type_1():
    """Transaction of type "second signature registration"
    """
    data = {
        'amount': 0,
        'asset': {
            'signature': {
                'publicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192'
            }
        },
        'fee': 500000000,
        'id': 'd6185acbd8ecae7781036e5a56f9b6e2e1b4ceda218aacfd514aeaf7e8b25b1e',
        'network': 30,
        'senderPublicKey': '037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c',
        'signature': '4dea6c361e3a95fdbf939b998cac021780206faa283d4c0d3ce203bc04dffb38c427894b543f7148673c9d9c8ba936fe774b709314e4ab77b393c5befd7ab6e8',
        'nonce': 1,
        'type': 1,
        'typeGroup': 1,
        'version': 3,
        'serialized': 'ff031e0100000001000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c0065cd1d0000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed1924dea6c361e3a95fdbf939b998cac021780206faa283d4c0d3ce203bc04dffb38c427894b543f7148673c9d9c8ba936fe774b709314e4ab77b393c5befd7ab6e8'
    }
    return data


@pytest.fixture
def transaction_type_2():
    """Transaction of type "delegate registration"
    """
    data = {
        'amount': 0,
        'asset': {
            'delegate': {
                'username': 'mr.delegate',
                'publicKey': '037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c'
            }
        },
        'fee': 2500000000,
        'id': 'ac34ed8e2608d08d596e60a4627cf45859a72ec573564d8dca5e67aef213e0b9',
        'network': 30,
        'senderPublicKey': '037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c',
        'signature': '20a80c34e5fde614b32e5f2c4edac2e1dda84eced2020162b9795aa1d3c323226f62034fd7e494f4b11b1e1045d9928bd5db3436c85b26decd49d101bea7aca1',
        'nonce': 1,
        'type': 2,
        'typeGroup': 1,
        'version': 3,
        'serialized': 'ff031e0100000002000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c00f9029500000000000b6d722e64656c656761746520a80c34e5fde614b32e5f2c4edac2e1dda84eced2020162b9795aa1d3c323226f62034fd7e494f4b11b1e1045d9928bd5db3436c85b26decd49d101bea7aca1'
    }
    # data = {
    #     'version': 2,
    #     'network': 30,
    #     'typeGroup': 1,
    #     'type': 2,
    #     'nonce': 1,
    #     'senderPublicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
    #     'fee': 2500000000,
    #     'asset': {
    #         'delegate': {
    #             'username': 'boldninja'
    #         }
    #     },
    #     'signature': 'eaf4b4dfd7903c32cf6c145ddf0744e86536719f5790b4286b08f1a10f0ad183bc601efc8a49a2a7b41758601a1793693afa1781cf0a63a8f72b08d5a1aaba1e',  # noqa
    #     'amount': 0,
    #     'id': 'cfd113d8cd9fd46b07030c14fac38c1d3fc0eca991e999eab9d0152ea96ab0dc',
    #     'serialized': 'ff02170100000002000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19200f90295000000000009626f6c646e696e6a61eaf4b4dfd7903c32cf6c145ddf0744e86536719f5790b4286b08f1a10f0ad183bc601efc8a49a2a7b41758601a1793693afa1781cf0a63a8f72b08d5a1aaba1e'  # noqa
    # }
    return data


@pytest.fixture
def transaction_type_3():
    """Transaction of type "vote"
    """
    data = {
        'amount': 0,
        'asset': {
            'votes': ['+034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192']
        },
        'fee': 100000000,
        'id': '66339c0b613c4cd4237e8f3dfeacb6f1a1b01f5677564d36bd2adbd775ac0c5c',
        'network': 30,
        'recipientId': 'DNSBvFTJtQpS4hJfLerEjSXDrBT7K6HL2o',
        'senderPublicKey': '037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c',
        'signature': '65a25eb5a49f0f6b1188007be3104e856ff42ae908b56ebb018d5d9348bf52532632e5efd04dfe383520acd34f8da0e4cd2caabe2434bfac012d5708ace7ef0a',
        'nonce': 1,
        'type': 3,
        'typeGroup': 1,
        'version': 3,
        'serialized': 'ff031e0100000003000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c00e1f50500000000000101034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19265a25eb5a49f0f6b1188007be3104e856ff42ae908b56ebb018d5d9348bf52532632e5efd04dfe383520acd34f8da0e4cd2caabe2434bfac012d5708ace7ef0a'
    }
    return data


@pytest.fixture
def transaction_type_4():
    """Transaction of type "multi signature registration"
    """
    data = {
        'amount': 0,
        'asset': {
            'multiSignature': {
                'min': 2,
                'publicKeys': ['0205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b896', '03df0a1eb42d99b5de395cead145ba1ec2ea837be308c7ce3a4e8018b7efc7fdb8', '03860d76b1df09659ac282cea3da5bd84fc45729f348a4a8e5f802186be72dc17f']
            }
        },
        'fee': 2000000000,
        'id': 'c6e132e124bdcc18291079308a1d1ced1c4673b31008c4b9e537774677349580',
        'network': 30,
        'senderPublicKey': '0205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b896',
        'signature': '84923dedf02195689feb29b688670f45f8694ee4cb5683b7d1b78bd7ec04761960ebac6ee3fa65611b6e3832df5e7269b3adbaaaa4fc77c9bb6ac3919110212b',
        'signatures': ['00feaf616793db83eb7108d01a77e029428fc754d62f576d2ca205f6be846692bae1457c1cd7bd3914b4c9c9fac94e5f3028e106e4a4143acb189558616a9f5191', '017691248d193e34193213bacc5fd322ae6006d35d824aa7b3a4643eb3d1ed29f2562fab314b6955cd88fd65ef659252f161d6eeb97c4df28522d3a4010a7b10f2', '02c2ab966eb816a7ee0995c01f64c42fa0b886967cf371d954d5feb72e079fa240982d2a0f3e899b09836360caa4a2c5c31933024658b5e895fbdeec8e06f668df'],
        'nonce': 1,
        'type': 4,
        'typeGroup': 1,
        'version': 3,
        'serialized': 'ff031e01000000040001000000000000000205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b89600943577000000000002030205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b89603df0a1eb42d99b5de395cead145ba1ec2ea837be308c7ce3a4e8018b7efc7fdb803860d76b1df09659ac282cea3da5bd84fc45729f348a4a8e5f802186be72dc17f84923dedf02195689feb29b688670f45f8694ee4cb5683b7d1b78bd7ec04761960ebac6ee3fa65611b6e3832df5e7269b3adbaaaa4fc77c9bb6ac3919110212b00feaf616793db83eb7108d01a77e029428fc754d62f576d2ca205f6be846692bae1457c1cd7bd3914b4c9c9fac94e5f3028e106e4a4143acb189558616a9f5191017691248d193e34193213bacc5fd322ae6006d35d824aa7b3a4643eb3d1ed29f2562fab314b6955cd88fd65ef659252f161d6eeb97c4df28522d3a4010a7b10f202c2ab966eb816a7ee0995c01f64c42fa0b886967cf371d954d5feb72e079fa240982d2a0f3e899b09836360caa4a2c5c31933024658b5e895fbdeec8e06f668df'
    }
    return data


@pytest.fixture
def transaction_type_5():
    """Transaction of type "ipfs"
    """
    data = {
        'amount': 0,
        'asset': {
            'ipfs': b'Cn8eVZg'
        },
        'fee': 500000000,
        'id': '96619bf765c72f38bee56d55c06270b4b361413ced10dac36ca934aa687c108c',
        'network': 30,
        'senderPublicKey': '037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c',
        'signature': 'f5749a4845fa89c62189c6e4958f205e9371be7ca04aa07b8e61bd25924dd8c0ee9885181bb7c55e4b110fb26ecd833b1a0d866f5c82e333d5499f4141ff4d39',
        'nonce': 1,
        'type': 5,
        'typeGroup': 1,
        'version': 3,
        'serialized': 'ff031e0100000005000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c0065cd1d000000000068656c6c6ff5749a4845fa89c62189c6e4958f205e9371be7ca04aa07b8e61bd25924dd8c0ee9885181bb7c55e4b110fb26ecd833b1a0d866f5c82e333d5499f4141ff4d39'
    }
    return data


@pytest.fixture
def transaction_type_6():
    """Transaction of type "multi payment"
    """
    data = {
        'amount': 0,
        'asset': {
            'payments': [{
                'amount': 1,
                'recipientId': 'DEMvpU4Qq6KvSzF3sRNjGCkm6Kj7cFfVaz'
            }, {
                'amount': 2,
                'recipientId': 'DQveGkK7te33dWJwHgKpGKDr5amxAE7PF4'
            }]
        },
        'fee': 10000000,
        'id': '8f148f2fdda47fde762edb24a37929d59af7906b7c455094266a5ed75dffba50',
        'network': 30,
        'senderPublicKey': '037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c',
        'signature': '4b09083a78f12d54b3b320b5793de8fafca95927ff368a6102e78bca87645efee92ca076c72062727e05f2e5033ad4980251894a696925588ff4a90665a6b231',
        'nonce': 1,
        'type': 6,
        'typeGroup': 1,
        'version': 3,
        'serialized': 'ff031e0100000006000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c809698000000000000020001000000000000001e65266cddfeec4b27a292a95d06f3d45bf9f3f61502000000000000001ed90798e15fd33f001b7c6c587dc78ae0c7d67d8c4b09083a78f12d54b3b320b5793de8fafca95927ff368a6102e78bca87645efee92ca076c72062727e05f2e5033ad4980251894a696925588ff4a90665a6b231'
    }
    return data


@pytest.fixture
def transaction_type_7():
    """Transaction of type "delegate resignation"
    """
    data = {
        'amount': 0,
        'asset': {
            'delegate': {
                'username': 'mr.delegate',
                'publicKey': '037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c'
            }
        },
        'fee': 2500000000,
        'id': '9ef3a1f29fc801388fa9bc94f8978fb6a2a3daf7196b653d8a1f1cfe054535bd',
        'network': 30,
        'senderPublicKey': '037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c',
        'signature': '6cb1b992ab627a169b5878126939cc6df1698560247c9a07cd78e1695bbe5dd86c9d3935b2028964d716006f7d602e1c4d7881704af2448cf63445fae12d5994',
        'nonce': 1,
        'type': 2,
        'typeGroup': 1,
        'version': 3,
        'serialized': 'ff031e0100000002000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c00f9029500000000000b6d722e64656c65676174656cb1b992ab627a169b5878126939cc6df1698560247c9a07cd78e1695bbe5dd86c9d3935b2028964d716006f7d602e1c4d7881704af2448cf63445fae12d5994'
    }
    return data


@pytest.fixture
def transaction_type_8():
    """Transaction of type "HTLC lock"
    """
    data = {
        'amount': 200000000,
        'asset': {
            'lock': {
                'secretHash': '1691053581dd80959b68ec8941898837790a43ec883bb32a2a9ea10edbb57c24',
                'expiration': {
                    'type': 1,
                    'value': 1573455822
                }
            }
        },
        'fee': 10000000,
        'id': '61c27654fba0cabdb7ba38ccf2c1dffe136f605572f465d9ec14d5001875ad65',
        'network': 30,
        'recipientId': 'DEMvpU4Qq6KvSzF3sRNjGCkm6Kj7cFfVaz',
        'senderPublicKey': '0201cd64fbf55b9de92471c9eb123eeedd9850ebed8fa6703df3af7a6b38631a2f',
        'signature': '6a35d659c7965d009254847cebf0d7b34a652a7e8599443e72ba414dd056864b95d05b55d0834dd859a0b1cc3eeee916b7938273fc2984bf9f813c5cf03a93f9',
        'nonce': 1,
        'type': 8,
        'typeGroup': 1,
        'version': 3,
        'serialized': 'ff031e01000000080001000000000000000201cd64fbf55b9de92471c9eb123eeedd9850ebed8fa6703df3af7a6b38631a2f80969800000000000000c2eb0b000000001691053581dd80959b68ec8941898837790a43ec883bb32a2a9ea10edbb57c2401ce07c95d1e65266cddfeec4b27a292a95d06f3d45bf9f3f6156a35d659c7965d009254847cebf0d7b34a652a7e8599443e72ba414dd056864b95d05b55d0834dd859a0b1cc3eeee916b7938273fc2984bf9f813c5cf03a93f9',
    }
    return data

@pytest.fixture
def transaction_type_9():
    """Transaction of type "HTLC claim"
    """
    data = {
        'amount': 0,
        'asset': {
            'claim': {
                'lockTransactionId': '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4',
                'unlockSecret': '6434323233626639336532303235303561366135303134323161383864396661'
            }
        },
        'fee': 0,
        'id': 'b2fa958105341c02aec73b607075e446bffa7e0c7f8de12cec3bf26b520222a4',
        'network': 30,
        'senderPublicKey': '037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c',
        'signature': 'ea298e4e68946caa1aaee12b566b5a9843bb0b91e97ddf16440fb360aeb4b293eb86e64a5ec1d37a64ca770c6806b1712f762d093b107bda7922ede6e26cbbb1',
        'nonce': 1,
        'type': 9,
        'typeGroup': 1,
        'version': 3,
        'serialized': 'ff031e0100000009000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c000000000000000000943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb46434323233626639336532303235303561366135303134323161383864396661ea298e4e68946caa1aaee12b566b5a9843bb0b91e97ddf16440fb360aeb4b293eb86e64a5ec1d37a64ca770c6806b1712f762d093b107bda7922ede6e26cbbb1'
    }
    return data

@pytest.fixture
def transaction_type_10():
    """Transaction of type "HTLC refund"
    """
    data = {
        'amount': 0,
        'asset': {
            'refund': {
                'lockTransactionId': '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4'
            }
        },
        'fee': 0,
        'id': '2b0149b4a31f67cd5b7afe2c968a39906fcebbc14611359a6d402b023b2cd4c7',
        'network': 30,
        'senderPublicKey': '037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c',
        'signature': 'a0e87b0ad0f2b31ad0b2c7e69589a2423c656f5e3a7d61ac03b73b634a404b15c6a3e7a188cabefe2b20ab1764310c7b9fb2ce8866b856642cdcc9561345494d',
        'nonce': 1,
        'type': 10,
        'typeGroup': 1,
        'version': 3,
        'serialized': 'ff031e010000000a000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c000000000000000000943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4a0e87b0ad0f2b31ad0b2c7e69589a2423c656f5e3a7d61ac03b73b634a404b15c6a3e7a188cabefe2b20ab1764310c7b9fb2ce8866b856642cdcc9561345494d'
    }
    return data


@pytest.fixture
def transaction_type_burn():
    """Transaction of type burn
    """
    data = {
        'amount': 2500000,
        'asset': {},
        'fee': 0,
        'id': '7e1dfa5cc0f70155530438d271885d39370fa0143287e8f6d40d2e67b9b6e366',
        'senderPublicKey': '03fe61f79ee50c5f45acfc37b33c3a5c10e2afe0204e3c8fa2a2d3d73a2b412360',
        'signature': 'ef071aa1c7631a6ace4227f583c78d922e938a1c3a8997a959e834e6b43ece34313a68dcf56ac606fb387006d9cbc962249376326c9dd84b81979eed5d1163d8',
        'nonce': 1,
        'type': 0,
        'typeGroup': 2,
        'version': 2,
        'network': 30,
        'serialized': 'ff021e020000000000010000000000000003fe61f79ee50c5f45acfc37b33c3a5c10e2afe0204e3c8fa2a2d3d73a2b412360000000000000000000a025260000000000ef071aa1c7631a6ace4227f583c78d922e938a1c3a8997a959e834e6b43ece34313a68dcf56ac606fb387006d9cbc962249376326c9dd84b81979eed5d1163d8'
    }
    return data


@pytest.fixture
def message():
    data = {
        'camelCase_pk': {
            'publicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
            'signature': '79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798f9ee8f2b718dc55e840f906c5071f63694ddeb35af8858f2a54cfdb3bd36fce1',  # noqa
            'message': 'Hello World'
        },

        'snake_case_pk': {
          'publickey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
          'signature': '79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798f9ee8f2b718dc55e840f906c5071f63694ddeb35af8858f2a54cfdb3bd36fce1',  # noqa
          'message': 'Hello World'
        },
        'passphrase': 'this is a top secret passphrase'
    }
    return data
