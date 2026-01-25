import string

x = input('Enter something')
x = x.title()
x = ''.join(ch for ch in x if ch not in string.punctuation and ch != ' ')
hashtag = '#' + x
if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
# print(len(hashtag))