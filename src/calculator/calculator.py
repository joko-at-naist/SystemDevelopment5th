class InvalidInputException(Exception):
    """Exception raised when input values are outside the valid range."""
    pass

class Calculator:
    MAX_VALUE = 1000000
    MIN_VALUE = -1000000

    def _validate_input(self, *values):
        for value in values:
            if not (self.MIN_VALUE <= value <= self.MAX_VALUE):
                raise InvalidInputException(
                    "Input value is outside of valid range"
                )

    def add(self, a, b):
        self._validate_input(a, b)
        return a + b

    def subtract(self, a, b):
        self._validate_input(a, b)
        return a - b

    def multiply(self, a, b):
        self._validate_input(a, b)
        return a * b

    def divide(self, a, b):
        self._validate_input(a, b)
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
