name = input("What is your name? ")
print(f"Hello {name}")

birth_year = input("Enter your birth year: ")
age = 2023 - int(birth_year)
print(age)

print('Python' in 'Python for beginners')

price = 5
print(price > 10 or price < 30)

if price > 30:
    print("Pricey!")
elif price > 10:
    print("Medium price")
else:
    print("Cheap!")

i = 1
while i <= 5:
    print(i)
    i = i + 1

names = ["Giordano", "Gaetano", "Germano", "Giornado"]
print(names[-1])

match age:
    case 5:
        print('Price is right')
    case other:
        print('Oh come on')

try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except ZeroDivisionError:
    print("Error")
