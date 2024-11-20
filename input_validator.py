def validate_integer_input(prompt):
    """
    Gets and validates integer input from user.

    Args:
        prompt (str): Message to display to user

    Returns:
        int: Valid integer input from user
    """
    while True:
        user_input = input(prompt)
        user_input = user_input.strip()

        if not user_input:
            print("Error: Empty input. Please enter a number.")
            continue

        try:
            number = int(user_input)
            return number

        except ValueError:
            if '.' in user_input:
                print("Error: Please enter a whole number (no decimal points).")
            elif any(char.isalpha() for char in user_input):
                print("Error: Letters are not allowed. Please enter a number.")
            elif any(not char.isdigit() and char != '-' for char in user_input):
                print("Error: Special characters are not allowed. Please enter a number.")
            else:
                print("Error: Invalid input. Please enter a valid integer.")