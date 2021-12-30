from num2roman.num2roman import Int2RomanConverter

roman_converter = Int2RomanConverter()
try:
    print(roman_converter.convert_int_to_roman(2.29))
except Exception as e:
    print(e)

try:
    print(roman_converter.convert_int_to_roman(1))
except Exception as e:
    print(e)

try:
    print(roman_converter.convert_int_to_roman(0))
except Exception as e:
    print(e)

try:
    print(roman_converter.convert_int_to_roman(5000))
except Exception as e:
    print(e)