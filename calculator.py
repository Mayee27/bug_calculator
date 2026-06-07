def divide(a, b):
    return a / b   # bug: crashes when b is 0

def add(a, b):
    return a + b

result = divide(10, 0)  # this will crash
print(result)
