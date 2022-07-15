# states = ['NY', 'PA', 'CA']
# states = ['New York', 'Pennsylvania', 'California']
# states = ['New York', 'NY', 'Pennsylvania', 'PA', 'California', 'CA']

states = {'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California'}

print(states['NY'])

# print(states['FL'])

people = ["Mattan", "Chris"]
# print(people[2])

print(type(states))
print(type(people))

print(states.get('FL', 'Not found'))
print(states.get('NY', 'Not found'))

print(states.keys())
print(states.values())

states['FL'] = 'Florida'
print(states)

# user = ['Mattan', 70, 10.5, 'Brown', 'Brown']
user = {'name': 'Mattan', 'height': 70, 'shoe size': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}

blog_post = {'title': '11 Sexy Uses for Dictionaries', 'body': 'Blah blah blah...'}

print(user['name'])
print(blog_post['title'])

# Dictionaries and Lists can be inside of each other

animal_sounds = {
    "cat": ["meow", "purr"],
    "dog": ["woof", "bark"],
    "fox": []
}

mattan = {'name': 'Mattan', 'height': 70, 'shoe size': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}
chris = {'name': 'Chris', 'height': 68, 'shoe size': 10, 'hair': 'Brown', 'eyes': 'Brown'}
sarah = {'name': 'Sarah', 'height': 72, 'shoe size': 8, 'hair': 'Brown', 'eyes': 'Brown'}

people = [mattan, chris, sarah]

print(people)

for person in people:
    print(person.get('height'))


