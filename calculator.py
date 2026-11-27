def divide(a, b):
    """Return a / b, raising ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")  # added explicit check
    return a / b  # now safe

def add(a, b):
    return a + b

# Demo code runs only when the module is executed directly
if __name__ == "__main__":
    result = divide(10, 2)  # example usage; no crash on import
    print(result)
