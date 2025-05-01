"""In Python, the if name == "main": statement is used to ensure that certain code only runs when the script
is executed directly, not when it's imported as a module."""


def main():
    print("Hello from main!")

if __name__ == "__main__":
    main()
    
    
"""    Explanation:

__name__ is a special built-in variable in Python.

When a file is run directly, __name__ is set to "__main__".

When the file is imported as a module in another script, __name__ is set to the module's name.

In Python, __name__ is called a special built-in variable because:

It is automatically defined by Python.

It has special meaning depending on how the script is run.

It uses double underscores before and after (this is often called a "dunder" name, short for Double UNDERscore).
"""