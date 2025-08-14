"""
Helpers methods
Author Shahnawaz
Not to be used in actual project this file should be excluded from commits
"""
import json
import random
import re
import string
from datetime import datetime

from faker import Faker


def default(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()  # Convert datetime to ISO format string
    raise TypeError(f"Type {type(obj)} not serializable")

# Function to convert a dictionary to a JSON string and prettify it


def dict_to_json_and_prettify(my_dict):
    return json.dumps(my_dict, sort_keys=True, indent=4, default=default)

# Function to generate a random email address


def random_email():
    fake = Faker()
    email = fake.email()
    return 'testqa_autotest_{email}'.format(email=email)

# Function to generate a random string of fixed length


def random_string(length=10):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters  # Includes both uppercase and lowercase letters
    return ''.join(random.choice(letters) for i in range(length))

# Function to generate a random number of fixed length


def random_number(length=10):
    """Generate a random number of fixed length."""
    return ''.join(random.choice(string.digits) for i in range(length))


# Function to validate an email address using regex
# This function checks if the email matches a specific pattern.
# It returns True if the email is valid, otherwise False.
# The regex pattern allows for a wide range of valid email formats.
# It includes support for special characters, domain names, and top-level domains.
# Note: This is a basic validation and may not cover all edge cases.
def valid_email(email):
    pattern = r"\"?([-a-zA-Z0-9+_.`?{}]+@[-a-zA-Z0-9+_.`?{}]+\.\w+)\"?"
    pattern = re.compile(pattern)
    if re.match(pattern, email):
        return True
    else:
        return False
