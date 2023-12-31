# TODO: Given a decimal integer convert it to binary string of 16 bits.


def decimal_to_binary(number: int) -> str:
    return "".join(str((number >> i) & 1) for i in reversed(range(16)))


def test():
    assert decimal_to_binary(0) == "0000000000000000"
    assert decimal_to_binary(1) == "0000000000000001"
    assert decimal_to_binary(2) == "0000000000000010"
    assert decimal_to_binary(3) == "0000000000000011"
    assert decimal_to_binary(4) == "0000000000000100"
    assert decimal_to_binary(65535) == "1111111111111111"
