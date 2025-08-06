class MyCustomError(Exception):
    pass

class ValueTooSmallError(MyCustomError):
    pass

class ValueTooLargeError(MyCustomError):
    pass

try:
    user_input = int(input(f"Please Enter A Number [5-15]:"))
    if user_input < 5:
        raise ValueTooSmallError(f"ValTooSmallError: The Number {user_input} is too small.")
    elif user_input >15:
        raise ValueTooLargeError(f"ValTooLargeError: The Number {user_input} is too large.")
    else:
        print(f"The Number {user_input} is within the allowed range.")
except ValueTooSmallError as e:
    print(e)
except ValueTooLargeError as e:
    print(e)