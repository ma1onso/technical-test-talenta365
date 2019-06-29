latin_alphabet = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'ñ',
    16: 'o',
    17: 'p',
    18: 'q',
    19: 'r',
    20: 's',
    21: 't',
    22: 'u',
    23: 'v',
    24: 'w',
    25: 'x',
    26: 'y',
    27: 'z',
}


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

        # More common case first
        if remainder != 0:
            excel_column_name.append(latin_alphabet[remainder].upper())
            number = int(number / alphabet_length)

        # If remainder is zero, letter is equal to Z
        elif remainder == 0:
            excel_column_name.append('Z')
            number = int(number / alphabet_length) - 1

    excel_column_name.reverse()
    return ''.join(excel_column_name)
