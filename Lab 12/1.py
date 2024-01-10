def check_range(value, min_val, max_val):
    assert min_val <= value <= max_val, f"Value {value} is not within the specified range [{min_val}, {max_val}]"

# Example usage:
try:
    check_range(15, 10, 20)  # This will not raise an error
    check_range(5, 10, 20)   # This will raise an AssertionError
except AssertionError as e:
    print(f"AssertionError: {e}")
