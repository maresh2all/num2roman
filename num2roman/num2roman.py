from enum import IntEnum

class Int2RomanConverter:
    '''
    Class Int2RomanConverter used to convert decimal numbers to roman numbers.
    Roman numerals limitations:
    - only positive integer between 1 and 4999.
    '''
    class RomanNumeral(IntEnum):
        '''
        Enum defining Roman numbers and their values. Listed in ascending order

        On top of the basic roman numeral (ie. I V X C D M)
        include IV IX XL XC CD CM combinations to simplify the rules
        '''
        I=1
        IV=4
        V=5
        IX=9
        X=10
        XL=40
        L=50
        XC=90
        C=100
        CD=400
        D=500
        CM=900
        M=1000

    def __private_convert_int_to_roman(self, n :int ) -> str:
        '''
        Private function receives an integer decimal number n and 
        returns that number as string representation in roman numerals
        This function gets called recursively.

            Parameters:
            n (int) decimal number to be converted

            Returns:
                (str) the number as a roman numeral
        '''
        # exit scenario when the rest is 0
        if n == 0:
            return ""
        # get the greatest roman divisor
        # taking advantage of the fact that since python 34 enums can be iterated in the order that they are defined
        g = [i for i in self.RomanNumeral if i<=n][-1]

        div= n // g # integer division
        mod = n % g 

        #      build number + recursive call with the rest
        return div * g.name + self.__private_convert_int_to_roman(mod)
    

    def convert_int_to_roman(self, n: int) -> str:
        '''
        Function receives an integer decimal number n and 
        returns that number as string representation in roman numerals
        Input get validated:
        - n has to be of type int
        - n greater than 0
        - n less than 5000

            Parameters:
            n (int) decimal number to be converted

            Returns:
                (str) the number as a roman numeral
        '''
        if not isinstance(n, int):
            raise TypeError("n was expecting an int, but received {0}".format(n))
        if n < 1 or n > 4999:
            raise ValueError("n was expected between 1 and 4999, but received {0}".format(n))

        return self.__private_convert_int_to_roman(n)
