import unittest
from num2roman.num2roman import Int2RomanConverter

class Int2RomanConverterTest(unittest.TestCase):

    def setUp(self):
        self.roman_converter = Int2RomanConverter()
        
    def test_convert_int_to_roman_type(self):
        '''check it doesn't accept  other inputs but int'''     
        with self.assertRaises(TypeError):
            self.roman_converter.convert_int_to_roman("string")
        
        with self.assertRaises(TypeError):
            self.roman_converter.convert_int_to_roman(2.2)

        with self.assertRaises(TypeError):
            self.roman_converter.convert_int_to_roman([99])

    def test_convert_int_to_roman_range(self):
        ''' check it doesn't accept input outside of range 1-4999'''    
        
        with self.assertRaises(ValueError):
            self.roman_converter.convert_int_to_roman(0)

        with self.assertRaises(ValueError):
            self.roman_converter.convert_int_to_roman(5000)        

    def test_convert_int_to_roman_value(self):
        ''' test with the basic roman numerals and other examples''' 
        for x in Int2RomanConverter.RomanNumeral:
            with self.subTest(i=x):
                self.assertEqual(self.roman_converter.convert_int_to_roman(x.value) , x.name, "Should be {}".format(x.name))

        self.assertEqual(self.roman_converter.convert_int_to_roman(15) , "XV", "Should be XV")

        self.assertEqual(self.roman_converter.convert_int_to_roman(99) , "XCIX", "Should be XCIX")

if __name__ == '__main__':
    unittest.main()