# Python Lists

*A list in Python is a collection of data. Lists can hold numbers, strings, boolean values (1 or 0), and other data structures (for instance, a list of lists!).*

## Python lists 

*Lists are basically that. Lists of things.*

- In `lists.py`:

```
the_count = [1, 2, 3, 4, 6]
stocks = ["AAPL", "GOOG", "TSLA"]
random_things = ["Puppies", 55, "Anthony Weiner", 1/2, ["Oh no", "A list inside a list"]]
```

*A list can have anything you want inside it: numbers, strings, even lists inside of lists. That last one is an example of nesting structure. And if that makes your head hurt, break it down into smaller pieces.*

## For Looping

*In this lesson, I'll show you how to loop over the elements in a list. This might come in handy in situations where you need to perform certain operations on each item in a list.*

*You can use the `for x in list` syntax to loop over a list. The x is your variable name for the thing in the list. So this:*

```py
# this for-loop goes through a list
for number in the_count:
    print("this is count", number)
```

- Returns this:

```bash
One-Months-Mac-mini:python mattangriffel$ python lists.py
this is count 1
this is count 2
this is count 3
this is count 4
this is count 5
One-Months-Mac-mini:python mattangriffel$
```

- You can also do this same thing with strings.

*Note that in your `for x in list` statement, the list has to already exist, but the X is a new variable your creating. So, if we were to ask `for i in random_list print ("Here's a random thing:", i)` then it would return everything in random_list, including the list nested inside random_list!*

## Removing Elements from a List

*Here's your next challenge: print out the squares of the numbers 1-10. If you need help, I'd suggest you learn how to use the following in Python: insert(), pop(), clear() and del.*

## Append and remove 

*You can add things to a list with the `append()` function, and remove things from a list with the `remove()` function.*

```py
# we can also build lists, first let's start with an empty one
people = []

people.append("Mattan")
people.append("Sarah")
people.append("Chris")

# now we can print them out too
print(people)

# and remove some
people.remove("Sarah")
print(people)
```

- This means that now when we use a for x in list function, we can set up like this: 

```py
for person in people:
    print("Person is:", person)
```

- And it will display our two people remaining in the list. 

## Challenge

**Here's a challenge:** print out the squares of the numbers 1-10.

## Home On The Python Range

*In this lesson, I'll show you how we can use a range function instead of a list. In Python, a range will give you a sequence of numbers that are between two provided values: a lower limit and an upper limit. The sequence starts at the lower limit and goes up to, but doesn't include the upper limit.*

*So now that you've had a chance to try it out yourself, let's look over how to print out a list of all the squares of each number from 1-10. You can do it by creating a list, like this:*

```py
# Challenge: Print out the square of the numbers 1 to 10
for number in range(1,2,3,4,5,6,7,8,9,10):
    print(number, "squared is", number * number)
```

*But in our quest to always keep our code as short and as clean as possible, let's look for another way to perform the same function. And in fact, there is: ranges.* 

## Ranges

*You can also use loops to do something a certain number of times with the range() function. It looks like this:* 

```py
# Challenge: Print out the square of the numbers 1 to 10
for number in range(1,10):
    print(number, "squared is", number * number)
```

- And comes out on the terminal like so: 

```bash
$ python loops.py
...
1 squared is 1
2 squared is 4
3 squared is 9
4 squared is 16
5 squared is 25
6 squared is 36
7 squared is 49
8 squared is 64
9 squared is 81
10 squared is 100
```

**Note:** *Ranges start at the first number and go up to (but don't include) the second number. So if you want to do something 10 times, you have to use range(1,11).*