from string import ascii_uppercase
from string import ascii_lowercase

class Diamond:
    def __init__(self, letter):
        if (not letter.isalpha()):
            raise ValueError("Input character is not a letter")
        if (len(letter) != 1):
            raise ValueError("Only one letter allowed")
        self.letter = letter
        if letter.isupper():
            self.alphabet = ascii_uppercase
        else:
            self.alphabet = ascii_lowercase
        position = self.alphabet.index(letter)
        self.alphabet = self.alphabet[:position + 1]
        self.width = (position + 1) * 2 - 1
        self.midpoint = position
        # create top half of diamond
        rows = []
        row = ""
        for i, letter in enumerate(self.alphabet):
            letter_spots = [self.midpoint + i, self.midpoint - i];
            # not super efficient for Python's immutable 
            # strings, but ok for this number of things
            for col in range(self.width):
                if (col in letter_spots):
                    row = row + letter
                else:
                    row = row + " "
            rows.append(row)
            row = ""
        self.completeDiamond = rows[:-1] + rows[::-1]
		
    def __str__(self):
        return_str = "";
        for row in self.completeDiamond:
            return_str = return_str + row + "\n";
        return return_str

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser('Letter Diamond Generator')
    parser.add_argument('-l', '--letter', type=str, default="G", help='Input letter, uppercase or lowercase [default G]')
    args = parser.parse_args()
    try:
        d = Diamond(args.letter)
        print d;
    except ValueError as e:
        print "Value Error: {0}".format(str(e))
        quit()
    except:
        print "Unexpected error. Exiting."