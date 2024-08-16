import re

def password_strength(password):
    """
    Assess the strength of a password based on multiple criteria.

    Parameters:
    password (str): The password to be assessed.

    Returns:
    str: The feedback on the password's strength.
    """
    # Criteria weights
    length_weight = 2
    uppercase_weight = 1
    lowercase_weight = 1
    numbers_weight = 1
    special_chars_weight = 1

    # Minimum length requirement
    min_length = 8

    # Assessing the password
    length_score = len(password) >= min_length
    uppercase_score = bool(re.search(r'[A-Z]', password))
    lowercase_score = bool(re.search(r'[a-z]', password))
    numbers_score = bool(re.search(r'[0-9]', password))
    special_chars_score = bool(re.search(r'[\W_]', password))

    # Calculate total score
    total_score = (length_score * length_weight +
                   uppercase_score * uppercase_weight +
                   lowercase_score * lowercase_weight +
                   numbers_score * numbers_weight +
                   special_chars_score * special_chars_weight)

    # Determine password strength
    if total_score == 6:
        feedback = "Strong"
    elif total_score >= 4:
        feedback = "Medium"
    else:
        feedback = "Weak"

    # Detailed feedback
    feedback_details = [
        f"Password Length: {'✔' if length_score else '✖'}",
        f"Uppercase Letters: {'✔' if uppercase_score else '✖'}",
        f"Lowercase Letters: {'✔' if lowercase_score else '✖'}",
        f"Numbers: {'✔' if numbers_score else '✖'}",
        f"Special Characters: {'✔' if special_chars_score else '✖'}"
    ]

    return feedback, feedback_details

def main():
    """
    Main function to run the password strength assessment tool.
    """
    print("Password Strength Assessment Tool")
    password = input("Enter the password to assess: ")
    
    feedback, feedback_details = password_strength(password)
    
    print(f"Password Strength: {feedback}")
    print("Details:")
    for detail in feedback_details:
        print(detail)

if __name__ == "__main__":
    main()
