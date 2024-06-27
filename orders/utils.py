

def format_phone_number(phone_number):
    # Remove any existing '+' from the phone number
    phone_number = phone_number.replace('+', '')
    # Check if the phone number starts with '0700' and prepend '+254'
    if phone_number.startswith('0700'):
        return '+254' + phone_number[1:]
    # Check if the phone number starts with '254' and prepend '+'
    elif phone_number.startswith('254'):
        return '+' + phone_number
    # Return the original phone number if it doesn't match the above cases
    return phone_number