def is_palindrome(text):
    y = text.lower()
    cleaned = ""
    for char in y:
        if char.isalnum():
            cleaned += char

    if cleaned == cleaned[::-1]:
        return True
    else:
        return False

text = input("Enter a text: ")
print(is_palindrome(text))


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")