latin_alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z'
]


def seek_letters(number):
    """ Given any positive integer number, get your value in letters. How does Excel.
    """
    if not type(number) in [int]:
        raise TypeError('number must be a integer')

    if number < 0:
        raise ValueError('The number cannot be negative')

    excel_column_name = []
    alphabet_length = len(latin_alphabet)

    while number > 0:
        remainder = number % alphabet_length

        excel_column_name.append(latin_alphabet[remainder - 1].upper())
        number = int(number / alphabet_length) - 1 if remainder == 0 else int(number / alphabet_length)

    return ''.join(excel_column_name[::-1])
