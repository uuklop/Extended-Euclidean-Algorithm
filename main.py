from algorithm import extended_euclidean
from input_validator import validate_integer_input
from display import show_welcome_message, show_results


def main():
    """Main function to run the Extended Euclidean Algorithm program."""
    try:
        show_welcome_message()

        # Get validated input
        first_number = validate_integer_input("\nEnter the first number: ")
        second_number = validate_integer_input("Enter the second number: ")

        # Check for zero inputs
        if first_number == 0 and second_number == 0:
            print("\nError: Both numbers cannot be zero as their GCD is undefined.")
            return

        # Calculate and display results
        gcd, coefficient1, coefficient2 = extended_euclidean(abs(first_number), abs(second_number))
        show_results(first_number, second_number, gcd, coefficient1, coefficient2)

    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    finally:
        print("\nThank you for using the Extended Euclidean Algorithm Calculator!")

if __name__ == "__main__":
    main()