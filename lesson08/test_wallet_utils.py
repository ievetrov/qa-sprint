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


def test_validate_amount_100000_is_allowed():
    # SPEC.md, строка 6: 100 000 ₽ включительно
    assert validate_amount(100000) is True


def test_validate_amount_100001_is_rejected():
    assert validate_amount(100001) is False


def test_calculate_fee_300_min_fee():
    assert calculate_fee(300) == 10.00


def test_calculate_fee_700_rounded_to_kopecks():
    # SPEC.md, строка 9: 700 → 10.50
    assert calculate_fee(700) == 10.50
