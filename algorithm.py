def extended_euclidean(first_number, second_number):
    """
    Finds the GCD of two numbers and coefficients that satisfy Bézout's identity.

    Args:
        first_number (int): First input number
        second_number (int): Second input number

    Returns:
        tuple: (gcd, coefficient1, coefficient2)
    """
    if first_number == 0:
        return second_number, 0, 1

    gcd, previous_x, previous_y = extended_euclidean(second_number % first_number, first_number)
    current_x = previous_y - (second_number // first_number) * previous_x
    current_y = previous_x

    return gcd, current_x, current_y
