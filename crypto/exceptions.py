class SolarCryptoException(Exception):
    pass


class SolarSerializerException(SolarCryptoException):
    """Raised when there's a serializer related issue"""


class SolarDeserializerException(SolarCryptoException):
    """Raised when there's a deserializer related issue"""


class SolarInvalidTransaction(SolarCryptoException):
    """Raised when transaction is not valid"""
