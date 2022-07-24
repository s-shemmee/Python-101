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