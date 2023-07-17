# TODO: Given a decimal integer convert it to binary string of 16 bits.


def decimal_to_binary(number: int) -> str:
    binary = str(number)
    padding = (16 - len(binary)) * "0"

    return padding + binary


def test():
    assert decimal_to_binary(0) == "0000000000000000"
    assert decimal_to_binary(1) == "0000000000000001"
