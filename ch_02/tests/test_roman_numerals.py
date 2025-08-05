from ..roman_numerals import to_roman_number
import pytest


def arabic_to_roman_number_map():
    return [
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV"),
        (5, "V"),
        (7, "VII"),
        (9, "IX"),
        (17, "XVII"),
        (40, "XL"),
        (90, "XC"),
        (400, "CD"),
        (444, "CDXLIV"),
        (500, "D"),
        (900, "CM"),
        (1000, "M"),
        (1666, "MDCLXVI"),
        (1971, "MCMLXXI"),
        (2018, "MMXVIII"),
        (2019, "MMXIX"),
        (2020, "MMXX"),
        (2021, "MMXXI"),
        (2022, "MMXXII"),
        (2023, "MMXXIII"),
        (2024, "MMXXIV"),
        (2025, "MMXXV"),

    ]


@pytest.mark.parametrize("n, roman_number", arabic_to_roman_number_map())
def test_to_roman_number(n, roman_number):
    assert to_roman_number(n) == roman_number