def check_number_type(func):
    """ Check if the number is not obj of type int, if so raise an Exception
    """
    def func_wrapper(number):
        if not type(number) in [int]:
            raise TypeError('number must be a integer')

        return func(number)

    return func_wrapper


def check_positive_integer(func):
    """ Check if the number is less than zero, if so raise an Exception
    """
    def func_wrapper(number):
        if number < 0:
            raise ValueError('The number cannot be negative')

        return func(number)

    return func_wrapper
