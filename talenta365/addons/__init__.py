from talenta365.addons.decorators import check_number_type, check_number_value

latin_alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z'
]


@check_number_value
@check_number_type
def seek_letters(number):
    """ Given any positive integer number, get your value in letters. How does Excel.
    """
    excel_column_name = []
    alphabet_length = len(latin_alphabet)

    while number > 0:
        remainder = (number - 1) % alphabet_length

        excel_column_name.append(latin_alphabet[remainder].upper())
        number = int((number - 1) / alphabet_length)

    return ''.join(excel_column_name[::-1])
