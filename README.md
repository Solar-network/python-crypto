# Solar Crypto Python Package

## Install

`pip install solar-crypto`

## Example usage

```py
from solar_crypto.configuration.network import set_network
from solar_crypto.networks.testnet import Testnet
from solar_crypto.transactions.builder.transfer import Transfer
set_network(Testnet)
transaction = Transfer(
    recipientId="D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib",
    amount=200000000,
)
transaction.set_nonce(1)
transaction.sign("super secret passphrase")
transaction.verify()
```

## Guide for contributing

1. Fork the repository on GitHub.
2. Run the tests to confirm they all pass on your system. If they don’t, you’ll need to investigate why they fail. If you’re unable to diagnose this yourself raise it as a bug report.
3. Make your change.
4. Write tests that demonstrate your bug or feature.
5. Run the entire test suite again, confirming that all tests pass including the ones you just added.
6. Send a GitHub Pull Request. GitHub Pull Requests are the expected method of code collaboration on this project.

## Documentation

You can find installation instructions and detailed instructions on how to use this package at the [dedicated documentation site](https://docs.solar.org/sdk/python/crypto/intro/).

## Security

If you discover a security vulnerability within this package, please send an e-mail to security@solar.org. All security vulnerabilities will be promptly addressed.

## Credits

This project exists thanks to all the people who [contribute](../../contributors).

## License

Please read the separate [LICENSE](LICENSE) file for details.
