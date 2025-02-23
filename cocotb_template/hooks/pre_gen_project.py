"""
Cookiecutter-Cocotb script generation validation

Author: Kerman Perez

"""
import sys
import re
import time

# Header
def show_header():
    """
    Shows the below defined header in terminal when executing this function
    """
    header = """
    *****************************************************************************************
    *          CocoTB Testbench Generator for IP Core Validation with Cookiecutter          *
    *                                 Automating Excellence!                                *
    *****************************************************************************************
    """
    print(header)


# Loading Screen
def loading_screen(message, duration=3):
    """Shows a message with ellipsis"""
    for _ in range(duration):
        for dots in range(4):
            sys.stdout.write(f'\r{message}{"." * dots}   ')  # Dynamic message
            sys.stdout.flush()
            time.sleep(0.5)  # Waits for half a second
    print("\n")


# Show initial header
show_header()

# Loading Screen initialised
loading_screen("Collecting and validating data", duration=2)

# Get the user's response
try:

    # Validate that the company name has no special characters
    if not re.match(r"^[a-zA-Z0-9_\-]+$", "{{cookiecutter.company}}"):
        print(
            "ERROR: The company name can only contain letters, numbers, underscores, and hyphens."
        )
        sys.exit(1)

    # Validate that the author's name has no special characters
    if not re.match(r"^[a-zA-Z0-9_\- ]+$", "{{cookiecutter.author}}"):
        print(
            "ERROR: The author name can only contain letters, "
            + "numbers, underscores, hyphens, and spaces."
        )
        sys.exit(1)

    # Validate that the project name has no special characters and replace spaces with underscores
    PROJECT_NAME = "{{cookiecutter.project_name}}"
    if not re.match(r"^[a-zA-Z0-9_\- ]+$", PROJECT_NAME):
        print(
            "ERROR: The project name can only contain letters, "
            + "numbers, underscores, and hyphens."
        )
        sys.exit(1)

    # Make sure there are no spaces and, if there are, convert them to underscores
    if " " in PROJECT_NAME:
        print("NOTE: Spaces in the project name have been replaced with underscores.")
        PROJECT_NAME = PROJECT_NAME.replace(" ", "_")

    # Validate that the project version is in X.Y.Z format
    if not re.match(r"^\d+\.\d+\.\d+$", "{{cookiecutter.project_version}}"):
        print("ERROR: The project version must follow the format X.Y.Z (e.g., 1.0.0).")
        sys.exit(1)

    # Validate that the number of tests is a positive integer
    try:
        NUMBER_OF_TESTS = int("{{cookiecutter.number_of_tests}}")
        if NUMBER_OF_TESTS <= 0:
            raise ValueError
    except ValueError:
        print("ERROR: Please enter a valid positive integer for the Test Number.")
        sys.exit(1)

    # Validate that the number of IP instances on the top_module is a positive integer
    try:
        NUMBER_OF_IP_INSTANCES = int("{{cookiecutter.number_of_ip_instances}}")
        if NUMBER_OF_IP_INSTANCES <= 0:
            raise ValueError
    except ValueError:
        print(
            "ERROR: Please enter a valid positive integer "
            + "for the number of instances of the IP core."
        )
        sys.exit(1)

    # Validate that the email has a valid format
    if not re.match(r"^[^@]+@[^@]+\.[^@]+$", "{{ cookiecutter.email }}"):
        print("ERROR: Please enter a valid email address")
        sys.exit(1)

    # If all validations pass...
    loading_screen("All data is valid! Proceeding with the project setup", duration=2)
    print("Validations completed successfully!\n")

except ValueError as e:
    loading_screen("Validation failed", duration=2)
    print(f"\n{e}")
    sys.exit(1)
