import printdiamond
from string import ascii_uppercase
from string import ascii_lowercase

for l in ascii_uppercase+ascii_lowercase:
    d = printdiamond.Diamond(l)
    print(d)