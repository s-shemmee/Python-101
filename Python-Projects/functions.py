def greet(name):
    return f"Hey {name}!"

def concatenate(word_one, word_two):
    return word_one + word_two

def age_in_dog_years(age):
    result = age * 7
    return result

print(greet('Mattan'))
print(greet('Chris'))

print(concatenate('Mattan', 'Griffel'))

print(age_in_dog_years(28))

print(concatenate(word_two='Mattan', word_one='Griffel'))

name = "Mattan"

def print_different_name():
    name = "Chris"
    print(name)

print(name)
print_different_name()
print(name)


def reverse(text):
    return text[::-1]

def uppercase_and_reverse(text):
    return reverse(text.upper())

print(uppercase_and_reverse("banana")) # ANANAB