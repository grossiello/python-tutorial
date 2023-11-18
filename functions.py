def hello_world():
    print("Hello World")


def multiply(x, y):
    return x * y


def occurrence(*vowels):
    return vowels.count('i')


hello_world()
print(multiply(2, 3))
print(occurrence('e', 'i', 'i', 'u', 'o', 'i'))
