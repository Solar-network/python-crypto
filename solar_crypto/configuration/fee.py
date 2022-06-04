from solar_crypto.constants import SOLAR_TRANSACTION_FEES, TRANSACTION_FEES, TRANSACTION_TYPE_GROUP

fees = TRANSACTION_FEES.copy()
solar_fees = SOLAR_TRANSACTION_FEES.copy()


def get_fee(transaction_type, type_group):
    """Get a fee for a given transaction type

    Args:
        transaction_type (int): transaction type for which we wish to get a fee
        type_group (int): transaction type group (TRANSACTION_TYPE_GROUP(Enum))

    Returns:
        int: transaction fee
    """
    if type_group == TRANSACTION_TYPE_GROUP.SOLAR.value:
        return solar_fees.get(transaction_type)
    return fees.get(transaction_type)


def set_fee(transaction_type, type_group, value):
    """Set a fee

    Args:
        transaction_type (int): transaction_type for which we wish to set a fee
        type_group (int): transaction type group (TRANSACTION_TYPE_GROUP(Enum))
        value (int): fee for a given transaction type
    """
    global fees
    global solar_fees

    if type_group == TRANSACTION_TYPE_GROUP.SOLAR.value:
        solar_fees[transaction_type] = value
    else:
        fees[transaction_type] = value
