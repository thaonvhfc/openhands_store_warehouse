def calculate(a, b):
    """Computes the sum, difference, quotient, and product of two numbers.
    Args:
        a: The first number.
        b: The second number.
    Returns:
        A dictionary containing the sum, difference, quotient, and product of a and b.
    """

    sum_result = a + b
    difference_result = a - b

    if b == 0:
        quotient_result = "Division by zero is not allowed."
    else:
        quotient_result = a / b

    product_result = a * b

    results = {
        "sum": sum_result,
        "difference": difference_result,
        "quotient": quotient_result,
        "product": product_result
    }

    return results


# Example usage:
a = 10
b = 5
results = calculate(a, b)

print(f"Sum: {results['sum']}")
print(f"Difference: {results['difference']}")
print(f"Quotient: {results['quotient']}")
print(f"Product: {results['product']}")

a = 5
b = 0
results = calculate(a, b)

print(f"Sum: {results['sum']}")
print(f"Difference: {results['difference']}")
print(f"Quotient: {results['quotient']}")
print(f"Product: {results['product']}")