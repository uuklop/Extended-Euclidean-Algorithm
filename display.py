def show_welcome_message():
    """Display welcome message and instructions"""
    print("\nExtended Euclidean Algorithm Calculator")
    print("======================================")
    print("\nThis program finds the GCD of two numbers and the coefficients")
    print("that satisfy Bézout's identity (ax + by = gcd).")
    print("\nPlease enter two integers:")


def show_results(first_number, second_number, gcd, coefficient1, coefficient2):
    """
    Display calculation results.
    """
    print("\nResults:")
    print("--------")
    print(f"First number: {first_number}")
    print(f"Second number: {second_number}")
    print(f"GCD: {gcd}")
    print(f"Coefficients: x = {coefficient1}, y = {coefficient2}")
    print("\nVerification:")
    print(f"{first_number} × ({coefficient1}) + {second_number} × ({coefficient2}) = {gcd}")

    verification = first_number * coefficient1 + second_number * coefficient2
    if abs(verification) == gcd:
        print("\nVerification successful! ✓")
    else:
        print("\nWarning: Verification failed! Please check the results.")