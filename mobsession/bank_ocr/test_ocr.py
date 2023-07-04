# ------------
# You work for a bank, which has recently purchased an ingenious machine to assist in
# reading letters and faxes sent in by branch offices.
# The machine scans the paper documents, and produces a file with a number of entries
# which each look like this:
#
#     _  _     _  _  _  _  _
#   | _| _||_||_ |_   ||_||_|
#   ||_  _|  | _||_|  ||_| _|
#
# Each entry is 4 lines long, and each line has 27 characters.
# The first 3 lines of each entry contain an account number written using pipes and
# underscores, and the fourth line is blank. Each account number should have 9 digits,
# all of which should be in the range 0-9. A normal file contains around 500 entries.
#
# Your first task is to write a program that can take this file and parse it into
# actual account numbers.
from __future__ import annotations

from dataclasses import dataclass
from typing import Self, Iterable


def test_digit_():
    assert list(
        Digit(
            " _|",
            "|_|",
            "|_|",
        ).alternatives()
    ) == [
        Digit(
            "|_|",
            "|_|",
            "|_|",
        )
    ]
    assert list(
        Digit(
            "  |",
            "|_|",
            "|_|",
        ).alternatives()
    ) == [
        Digit(
            "| |",
            "|_|",
            "|_|",
        ),
        Digit(
            " _|",
            "|_|",
            "|_|",
        ),
    ]
    assert list(
        Digit(
            "   ",
            "   ",
            "   ",
        ).alternatives()
    ) == [
        Digit(
            "|  ",
            "   ",
            "   ",
        ),
        Digit(
            " _ ",
            "   ",
            "   ",
        ),
        Digit(
            "  |",
            "   ",
            "   ",
        ),
        Digit(
            "   ",
            "|  ",
            "   ",
        ),
        Digit(
            "   ",
            " _ ",
            "   ",
        ),
        Digit(
            "   ",
            "  |",
            "   ",
        ),
        Digit(
            "   ",
            "   ",
            "|  ",
        ),
        Digit(
            "   ",
            "   ",
            " _ ",
        ),
        Digit(
            "   ",
            "   ",
            "  |",
        ),
    ]


def replace(text, index, value):
    return text[:index] + value + text[(index + 1) :]


@dataclass(unsafe_hash=True)
class Digit:
    top: str
    middle: str
    bottom: str
    value: str = None

    def __post_init__(self):
        self.value = "*".join([self.top, self.middle, self.bottom])

    def alternatives(self) -> Iterable[Digit]:
        for i, c in enumerate(self.value):
            if i % 4 in [0, 2] and c == " ":
                yield Digit(*replace(self.value, i, "|").split("*"))

            if i % 4 == 1 and c == " ":
                yield Digit(*replace(self.value, i, "_").split("*"))

    @classmethod
    def zero(cls) -> Self:
        return cls(
            " _ ",
            "| |",
            "|_|",
        )

    @classmethod
    def one(cls) -> Self:
        return cls(
            "   ",
            "  |",
            "  |",
        )

    @classmethod
    def two(cls) -> Self:
        return cls(
            " _ ",
            " _|",
            "|_ ",
        )

    @classmethod
    def three(cls) -> Self:
        return cls(
            " _ ",
            " _|",
            " _|",
        )

    @classmethod
    def four(cls) -> Self:
        return cls(
            "   ",
            "|_|",
            "  |",
        )

    @classmethod
    def five(cls) -> Self:
        return cls(
            " _ ",
            "|_ ",
            " _|",
        )

    @classmethod
    def six(cls) -> Self:
        return cls(
            " _ ",
            "|_ ",
            "|_|",
        )

    @classmethod
    def seven(cls) -> Self:
        return cls(
            " _ ",
            "  |",
            "  |",
        )

    @classmethod
    def eight(cls) -> Self:
        return cls(
            " _ ",
            "|_|",
            "|_|",
        )

    @classmethod
    def nine(cls) -> Self:
        return cls(
            " _ ",
            "|_|",
            " _|",
        )


@dataclass
class ASCIINumber:
    digits: [Digit]

    _ASCII_TO_DIGIT = {
        Digit.zero(): "0",
        Digit.one(): "1",
        Digit.two(): "2",
        Digit.three(): "3",
        Digit.four(): "4",
        Digit.five(): "5",
        Digit.six(): "6",
        Digit.seven(): "7",
        Digit.eight(): "8",
        Digit.nine(): "9",
    }

    @classmethod
    def parse(cls, raw: str) -> Self:
        top, middle, bottom = raw.strip("\n").split("\n")

        return cls(
            [
                Digit(*raw)
                for raw in zip(
                    cls.cut(top),
                    cls.cut(middle),
                    cls.cut(bottom),
                )
            ]
        )

    def as_string(self) -> str:
        return "".join(self._ASCII_TO_DIGIT.get(digit, "?") for digit in self.digits)

    @staticmethod
    def cut(text: str, chunk_size: int = 3) -> [str]:
        return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]

    def alternatives(self) -> Iterable[ASCIINumber]:
        for i, digit in enumerate(self.digits):
            for alternative in digit.alternatives():
                if alternative in self._ASCII_TO_DIGIT:
                    yield ASCIINumber(
                        self.digits[:i] + [alternative] + self.digits[i + 1 :]
                    )


def test_alternatives():
    assert [
        alt.as_string()
        for alt in ASCIINumber.parse(
            (
                "                           \n"
                "  |  |  |  |  |  |  |  |  |\n"
                "  |  |  |  |  |  |  |  |  |\n"
            ),
        ).alternatives()
    ] == [
        "711111111",
        "171111111",
        "117111111",
        "111711111",
        "111171111",
        "111117111",
        "111111711",
        "111111171",
        "111111117",
    ]


@dataclass
class AccountNumber:
    value: str

    def generate_status(self) -> str:
        if len(self.value) != 9:
            return self.value + " ILL"

        if not self.value.isdigit():
            return self.value + " ILL"

        if not self._is_valid():
            return self.value + " ERR"

        return self.value

    def _is_valid(self) -> bool:
        result = sum(i * int(digit) for i, digit in enumerate(reversed(self.value), 1))

        return result % 11 == 0


def test_should_parse():
    assert (
        ASCIINumber.parse(
            (
                " _  _  _  _  _  _  _  _  _ \n"
                "| || || || || || || || || |\n"
                "|_||_||_||_||_||_||_||_||_|\n"
            ),
        ).as_string()
        == "000000000"
    )
    assert (
        ASCIINumber.parse(
            (
                "                           \n"
                "  |  |  |  |  |  |  |  |  |\n"
                "  |  |  |  |  |  |  |  |  |\n"
            ),
        ).as_string()
        == "111111111"
    )
    assert (
        ASCIINumber.parse(
            (
                " _  _  _  _  _  _  _  _  _ \n"
                " _| _| _| _| _| _| _| _| _|\n"
                "|_ |_ |_ |_ |_ |_ |_ |_ |_ \n"
            ),
        ).as_string()
        == "222222222"
    )
    assert (
        ASCIINumber.parse(
            (
                " _  _  _  _  _  _  _  _  _ \n"
                " _| _| _| _| _| _| _| _| _|\n"
                " _| _| _| _| _| _| _| _| _|\n"
            ),
        ).as_string()
        == "333333333"
    )
    assert (
        ASCIINumber.parse(
            (
                "                           \n"
                "|_||_||_||_||_||_||_||_||_|\n"
                "  |  |  |  |  |  |  |  |  |\n"
            ),
        ).as_string()
        == "444444444"
    )
    assert (
        ASCIINumber.parse(
            (
                " _  _  _  _  _  _  _  _  _ \n"
                "|_ |_ |_ |_ |_ |_ |_ |_ |_ \n"
                " _| _| _| _| _| _| _| _| _|\n"
            ),
        ).as_string()
        == "555555555"
    )
    assert (
        ASCIINumber.parse(
            (
                " _  _  _  _  _  _  _  _  _ \n"
                "|_ |_ |_ |_ |_ |_ |_ |_ |_ \n"
                "|_||_||_||_||_||_||_||_||_|\n"
            ),
        ).as_string()
        == "666666666"
    )
    assert (
        ASCIINumber.parse(
            (
                " _  _  _  _  _  _  _  _  _ \n"
                "  |  |  |  |  |  |  |  |  |\n"
                "  |  |  |  |  |  |  |  |  |\n"
            ),
        ).as_string()
        == "777777777"
    )
    assert (
        ASCIINumber.parse(
            (
                " _  _  _  _  _  _  _  _  _ \n"
                "|_||_||_||_||_||_||_||_||_|\n"
                "|_||_||_||_||_||_||_||_||_|\n"
            ),
        ).as_string()
        == "888888888"
    )
    assert (
        ASCIINumber.parse(
            (
                " _  _  _  _  _  _  _  _  _ \n"
                "|_||_||_||_||_||_||_||_||_|\n"
                " _| _| _| _| _| _| _| _| _|\n"
            ),
        ).as_string()
        == "999999999"
    )
    assert (
        ASCIINumber.parse(
            (
                " _     _  _     _  _  _  _  _ \n"
                "| |  | _| _||_||_ |_   ||_||_|\n"
                "|_|  ||_  _|  | _||_|  ||_| _|\n"
            ),
        ).as_string()
        == "0123456789"
    )
    assert (
        ASCIINumber.parse(
            (
                "    _  _  _  _  _  _     _ \n"
                "|_||_|| || ||_   |  |  | _ \n"
                "  | _||_||_||_|  |  |  | _|\n"
            ),
        ).as_string()
        == "49006771?"
    )


def test_should_generate_account_number_status():
    assert AccountNumber("000000000").generate_status() == "000000000"
    assert AccountNumber("100000010").generate_status() == "100000010"
    assert AccountNumber("003000001").generate_status() == "003000001"
    assert AccountNumber("103000011").generate_status() == "103000011"
    assert AccountNumber("000022500").generate_status() == "000022500"
    assert AccountNumber("010102000").generate_status() == "010102000"
    assert AccountNumber("000000051").generate_status() == "000000051"
    assert AccountNumber("100000011").generate_status() == "100000011 ERR"
    assert AccountNumber("111111111").generate_status() == "111111111 ERR"
    assert AccountNumber("49006771?").generate_status() == "49006771? ILL"


# TODO
# 1. Simplify digit: add join method for top, middle, bottom
# 2. Validate alternative numbers
# 3. rename Digit
