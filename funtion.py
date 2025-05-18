def greet_user(name):
    """Function to greet the user by their name."""
    if not name:
        return "Hello, Guest!"
    return f"Hello, {name}! Welcome to the program."

# Example usage:
print(greet_user("Abhishek"))
print(greet_user(""))
