import keyword
import string

x = input('Enter something')
if(
        x
        and x.islower()
        and not x[0].isdigit()
        and " " not in x
        and not any (char in string.punctuation and char != "_" for char in x)
        and x not in keyword.kwlist
        and x.count('_')<2
):
    print('true')
else:
    print('false')