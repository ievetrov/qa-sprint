from wallet_utils import format_amount, validate_amount, calculate_fee


def test_format_amount_1000_has_two_decimals():
    # Arrange
    amount = 1000
    # Act
    result = format_amount(amount)
    # Assert
    assert result == "1000.00"


# Ваши тесты пишутся ниже, каждый — отдельной функцией с именем test_*.
# Ожидаемые значения берутся из таблицы в SPEC.md и больше ниоткуда.

def test_format_amount_1234_5():
    assert format_amount(1234.5) == "1234.50"


def test_validate_amount_zero_is_rejected():
    assert validate_amount(0) is False


def test_validate_amount_100001_is_rejected():
    assert validate_amount(100001) is False


def test_calculate_fee_300_min_fee():
    assert calculate_fee(300) == 10.00


def test_calculate_fee_1000():
    assert calculate_fee(1000) == 15.00


def test_calculate_fee_2000():
    assert calculate_fee(2000) == 30.00
