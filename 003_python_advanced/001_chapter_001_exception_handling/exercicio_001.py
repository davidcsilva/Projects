"""
Python Advanced - Chapter 1: Exception Handling
Examples demonstrating basic to advanced exception handling techniques.
"""

# ==============================================================================
# 1. Basic try / except / else / finally
# ==============================================================================


def safe_division(a: float, b: float) -> float | None:
    """
    Demonstrates the full try-except-else-finally structure:
      - try: code that may raise an exception
      - except: executed only if a matching exception occurs
      - else: executed only if NO exception occurred in try
      - finally: always executed (great for cleanup)
    """
    print(f"\n--- Calculating {a} / {b} ---")
    result = None
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"[ERROR] Cannot divide by zero! ({e})")
    except TypeError as e:
        print(f"[ERROR] Invalid data type passed: {e}")
    else:
        print(f"[SUCCESS] Division result: {result}")
    finally:
        print("[FINALLY] Completed attempt (cleanup operations happen here).")
    return result


# ==============================================================================
# 2. Catching Multiple Exceptions in One Block & Inspecting Errors
# ==============================================================================
def parse_int_item(items: list[str], index: int) -> int | None:
    """
    Demonstrates catching multiple exception types together and extracting error info.
    """
    try:
        val = items[index]
        return int(val)
    except (IndexError, ValueError) as err:
        print(
            f"[HANDLED] Could not parse item at index {index}: {type(err).__name__} -> {err}")
        return None


# ==============================================================================
# 3. Custom Exceptions & Raising Exceptions
# ==============================================================================
class NegativeValueError(ValueError):
    """Custom exception raised when a value is unexpectedly negative."""

    def __init__(self, value: float, message: str = "Value cannot be negative"):
        self.value = value
        self.message = f"{message}: {value}"
        super().__init__(self.message)


def calculate_square_root(x: float) -> float:
    """Calculates square root and raises a custom exception if negative."""
    if x < 0:
        raise NegativeValueError(x)
    return x ** 0.5


# ==============================================================================
# 4. Exception Chaining (raise ... from ...)
# ==============================================================================
class DataProcessingError(Exception):
    """High-level domain exception."""
    pass


def process_record(raw_number: str) -> float:
    """
    Wraps low-level errors into a higher-level domain error while preserving the traceback.
    """
    try:
        num = float(raw_number)
        return calculate_square_root(num)
    except (ValueError, NegativeValueError) as original_error:
        # 'raise ... from' preserves the original cause in __cause__
        raise DataProcessingError(
            "Failed to process data record") from original_error


# ==============================================================================
# Demonstration Execution
# ==============================================================================
if __name__ == "__main__":
    print("=================== 1. Basic try/except/else/finally ===================")
    safe_division(10, 2)   # Success case (runs try -> else -> finally)
    safe_division(10, 0)   # ZeroDivisionError (runs try -> except -> finally)
    safe_division(10, "x")  # TypeError (runs try -> except -> finally)

    print("\n=================== 2. Multiple Exceptions ===================")
    sample_list = ["42", "hello", "100"]
    parse_int_item(sample_list, 0)   # Valid -> 42
    parse_int_item(sample_list, 1)   # ValueError -> invalid literal for int()
    parse_int_item(sample_list, 10)  # IndexError -> list index out of range

    print("\n=================== 3. Custom Exceptions ===================")
    try:
        print("Square root of 25:", calculate_square_root(25))
        calculate_square_root(-9)
    except NegativeValueError as err:
        print(f"Caught custom exception: {err} (value was {err.value})")

    print("\n=================== 4. Exception Chaining ===================")
    try:
        process_record("invalid_number")
    except DataProcessingError as err:
        print(f"Caught: {err}")
        print(f"Original cause: {repr(err.__cause__)}")
