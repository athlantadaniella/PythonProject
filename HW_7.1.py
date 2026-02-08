x = input("Enter yor name: ")
y = int(input("Enter your age: "))

def say_hi(x,y):
    say_hi = f"Hi. My name is {x} and I'm {y} years old"
    return say_hi
print(say_hi(x,y))


assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')
