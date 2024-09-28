def is_alphanumeric_with_spaces(s):
    return all(char.isalnum() or char.isspace() for char in s)
