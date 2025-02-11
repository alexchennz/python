import random
import string


def generate_password(length=12, use_letters=True, use_numbers=True, use_symbols=True):
    """
    Generate a random password based on specified criteria
    
    Args:
        length (int): Length of the password
        use_letters (bool): Include letters (a-z, A-Z)
        use_numbers (bool): Include numbers (0-9)
        use_symbols (bool): Include special characters
    
    Returns:
        str: Generated password
    """
    # Define character sets
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    
    # Create the character pool based on user preferences
    char_pool = ''
    if use_letters:
        char_pool += letters
    if use_numbers:
        char_pool += numbers
    if use_symbols:
        char_pool += symbols
        
    # Ensure at least one character set is selected
    if not char_pool:
        raise ValueError("At least one character set must be selected")
    
    # Generate password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password


def main():
    try:
        # Example usage
        print("=== Password Generator ===")
        
        # Get user preferences
        length = int(input("Enter password length (default 12): ") or 12)
        use_letters = input("Include letters? (Y/n): ").lower() != 'n'
        use_numbers = input("Include numbers? (Y/n): ").lower() != 'n'
        use_symbols = input("Include symbols? (Y/n): ").lower() != 'n'
        
        # Generate and display password
        password = generate_password(
            length=length,
            use_letters=use_letters,
            use_numbers=use_numbers,
            use_symbols=use_symbols
        )
        
        print("\nGenerated Password:", password)
        
    except ValueError as e:
        print("Error:", str(e))
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")


if __name__ == "__main__":
    main()
