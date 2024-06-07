import re

def check_password_complexity(password):
    """
    Checks the complexity of a given password.

    Parameters:
    - password: str, the password to be checked.

    Returns:
    - dict: A dictionary containing the results of the complexity check.
    """
    # Initialize criteria checks
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[@$!%*?&#]', password) is not None

    # Calculate overall strength
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])
    strength = "Very Weak"
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"

    # Results dictionary
    result = {
        "Length (at least 8 characters)": length_criteria,
        "Uppercase letter": uppercase_criteria,
        "Lowercase letter": lowercase_criteria,
        "Digit": digit_criteria,
        "Special character": special_char_criteria,
        "Overall strength": strength
    }

    return result

def main():
    print("Password Complexity Checker")
    print("===========================")

    while True:
        # User input for password
        password = input("Enter a password to check: ").strip()

        # Check password complexity
        result = check_password_complexity(password)

        # Display results
        print("\nPassword Complexity Results:")
        for criteria, met in result.items():
            if criteria != "Overall strength":
                print(f"{criteria}: {'✔️' if met else '❌'}")
        print(f"Overall strength: {result['Overall strength']}\n")

        # Option to check another password or quit
        another = input("Would you like to check another password? (y/n): ").strip().lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()

