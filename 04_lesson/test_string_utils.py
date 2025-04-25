import pytest

from string_utils import StringUtils

string_utils = StringUtils()  # Экземпляр класса


# Тесты для capitalize
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "Skypro"),
        ("hello world", "Hello world"),
        ("python", "Python"),
    ],
)
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("123abc", "123abc"),
        ("", ""),
        ("   ", "   "),
    ],
)
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Тесты для trim
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   ASD", "ASD"),
        ("    367", "367"),
        ("   ", ""),
    ],
)
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("text", "text"),
        ("text  ", "text  "),
        ("", ""),
    ],
)
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# Тесты для contains
@pytest.mark.positive
@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("ASDF", "S", True),
        ("8731", "7", True),
        ("27 apr 2022", " ", True),
    ],
)
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("", "a", False),
        ("GHOL", "g", False),
        ("2469", "3", False),
    ],
)
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


# Тесты для delete_symbol
@pytest.mark.positive
@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("helpo", "o", "help"),
        ("1235", "1", "235"),
        ("asd kl", " ", "asdkl"),
    ],
)
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("helpo", "a", "helpo"),
        ("1235", "9", "1235"),
        ("", "o", ""),
    ],
)
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
