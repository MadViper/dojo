# TODO: Given a decimal integer convert it to binary string of 16 bits.


def decimal_to_binary(number: int) -> str:
    padding = 15 * "0"
    return padding + str(number)


def test():
    assert decimal_to_binary(0) == "0000000000000000"
