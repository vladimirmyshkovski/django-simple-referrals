from uuid import UUID


def validate_uuid4(uuid_string):

    """
    Validate that a UUID string is in
    fact a valid uuid4.
    Happily, the uuid module does the actual
    checking for us.
    It is vital that the 'version' kwarg be passed
    to the UUID() call, otherwise any 32-character
    hex string is considered valid.
    """
    try:
        UUID(uuid_string, version=4)
    except ValueError:
        # If it's a value error, then the string
        # is not a valid hex code for a UUID.
        return False
    except TypeError:
        # If it's a type error, then the string
        # is None or something else
        return False

    return uuid_string
