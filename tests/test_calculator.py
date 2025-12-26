"""
Test suite for the Calculator class.
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from calculator.calculator import Calculator, InvalidInputException


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_too_large_values(self):
        """Test adding values that exceed the maximum limit."""
        calc = Calculator()
        with pytest.raises(InvalidInputException) as exc_info:
            calc.add(1000001, 1)
        assert str(exc_info.value) == "Input value is outside of valid range"


    def test_add_boundary_min_value(self):
        """Test adding exact minimum value (境界値テスト: 下限)."""
        calc = Calculator()
        # -1,000,000 ちょうどは「正常値」として扱われるべき
        # オリジナルコード: OK
        # ミュータント(<): NG (ここでテストが落ちる＝ミュータント検知！)
        result = calc.add(calc.MIN_VALUE, 0)
        assert result == calc.MIN_VALUE

    def test_add_boundary_max_value(self):
        """Test adding exact maximum value (境界値テスト: 上限)."""
        calc = Calculator()
        # 1,000,000 ちょうどは「正常値」として扱われるべき
        result = calc.add(calc.MAX_VALUE, 0)
        assert result == calc.MAX_VALUE


    def test_add_toosmall_numbers(self):
        """Test adding too small numbers (下限超過)."""
        calc = Calculator()
        with pytest.raises(InvalidInputException) as exc_info:
            calc.add(-1000001, 0)
        assert str(exc_info.value) == "Input value is outside of valid range"



    def test_add_negative_numbers(self):
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self):
        """Test adding positive number with zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)

    # TestAddition クラスに追加

    def test_add_second_arg_invalid(self):
        """Test when only the second argument is invalid."""
        calc = Calculator()
        # a=1 (OK), b=1000001 (NG)
        with pytest.raises(InvalidInputException) as exc_info:
            calc.add(1, 1000001)
        assert str(exc_info.value) == "Input value is outside of valid range"


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 6
        b = 9
        expected = 3
        result = calc.subtract(b, a)
        assert result == expected


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 8
        b = 2
        expected = 16
        result = calc.multiply(a, b)
        assert result == expected


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 10
        b = 2
        expected = 5
        result = calc.divide(a, b)
        assert result == expected




