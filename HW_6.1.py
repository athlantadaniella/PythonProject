import string

text1 = input('Enter letter 1:')
text2 = input('Enter letter 2:')
text3 = text1 + '-' + text2
print(text3)
start, end = text3.split('-')

letters = string.ascii_letters

start_index = letters.index(start)
end_index = letters.index(end)

result = letters[start_index:end_index + 1]
print(result)