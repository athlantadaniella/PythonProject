x = input("Enter yor sentence: ")

def correct_sentence(x):
    x = x[:1].upper() + x[1:]
    if not x.endswith('.'):
        x += '.'
    return x

result = correct_sentence(x)
print(result)

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
