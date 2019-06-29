from django.test import TestCase

from talenta365.addons import seek_letters


class SeekLettersCase(TestCase):

    def test_seek_letters(self):
        self.assertEqual(seek_letters(69), 'BÑ')
        self.assertEqual(seek_letters(28), 'AA')
        self.assertEqual(seek_letters(54), 'AZ')
        self.assertEqual(seek_letters(55), 'BA')
        self.assertEqual(seek_letters(16), 'O')
        self.assertEqual(seek_letters(15), 'Ñ')
        self.assertEqual(seek_letters(14), 'N')
        self.assertEqual(seek_letters(13), 'M')
        self.assertEqual(seek_letters(2), 'B')
        self.assertEqual(seek_letters(1), 'A')

    def test_values_seek_letters(self):
        self.assertRaises(ValueError, seek_letters, -10)

    def test_types_seek_letters(self):
        self.assertRaises(TypeError, seek_letters, 'n')
