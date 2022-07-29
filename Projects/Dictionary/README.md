# Consult The Dictionary

*In this lesson, we look at Python dictionaries. A dictionary is an unordered, changeable and indexed collection that doesn't allow for duplicate members. It is similar to a list, in that it is a collection of objects, but the main difference between the two is that a list is ordered while a dictionary isn't.*

*We already have a lot of different data types, but dictionaries are super important in order to do a lot of really useful things in Python. Dictionaries are basically lists - but lists go in order. With dictionaries, we use can look up something using a special key (basically a string).*

- Create a file called `dictionaries.py`. Inside, follow this syntax: 

```py
# states = ['NY', 'PA', 'CA']
# states = ['New York', 'Pennsylvania', 'California']
# states = ['New York', 'NY', 'Pennsylvania', 'PA', 'California', 'CA']

states = {'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California'}
```

*Voila! You've just created a dictionary. **The key value pair** are the things on either side of the colon. Note that **the key** is the thing to the left of the colon, and it has to be a string. But the thing on the right is the **value**, and that can be any data type.*

*This is the main difference between dictionaries and lists. You can access anything inside of a dictionary using the key (a string). With lists, you have to access things by number. Lists also guarantee they'll return in a particular order, and dictionaries do not. This makes them fast.* 

# Searching a dictionary 

*To pull out the value from a dictionary, we simply print the key.* 

*If you try to access something that isn't in the dictionary, you'll get a key error. And if you ever get confused about what something is - a dictionary or a list - you can always use the `type()` function.* 

*You can search for things in dictionaries using `.get()`. It lets you look something up without returning a key error.* 

*You're also able to get all the keys in a given dictionary by printing `.keys()`.*

*Adding things to a dictionary is actually pretty easy. And that will set the key, even if it doesn't already exist.* 

*Dictionaries are super useful to specify the information. Compare the list, which is commented out, with the dictionary, which keeps track of Mattan's details in a much more robust way:*

```py
# user = ['Mattan', 70, 10.5, 'Brown', 'Brown']
user = {'name': 'Mattan', 'height': 70, 'shoe size': 10.5, 'hair': 'Brown', 'eyes': 'Brown'
```

# You've Got A List In My Dictionary!

*In this lesson, I'll show you how to iterate and access values in objects, as well as show you how to avoid errors.*

## Lists inside of dictionaries

*Your gonna see lots of lists inside dictionaries and dictionaries inside lists. This can get kind of crazy but stick with me.* 

```py
animal_sounds = {

   "cat": ["meow", "purr"],

   "dog": ["woof", "bark"],

   "fox": []

}
```

- We can do this for users as well. 

```py
mattan = {'name': 'Mattan', 'height': 70, 'shoe size': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}

chris = {'name': 'Chris', 'height': 68, 'shoe size': 10, 'hair': 'Brown', 'eyes': 'Brown'}

sarah = {'name': 'Sarah', 'height': 72, 'shoe size': 8, 'hair': 'Brown', 'eyes': 'Brown'}
```

## Create a list

- But now let's create a list: 

```py
people = [mattan, chris, sarah]

print(people)
```

*Remember that these variables inside our list are now all dictionaries. If you print the list, you'll get all the dictionaries.* 

*If you wanted to just print out the height of each person, you can loop over the list people, and realize that they all have the same keys. So you could use `person['height']` to get their height.* 

## Loops 

- The loop looks like this:

```py
for person in people:

print(person['height'])
```

*Note this only works because I know all the dictionaries have the 'height' key. A safer option might be:*

```py
for person in people:

print(person.get('height'))
```