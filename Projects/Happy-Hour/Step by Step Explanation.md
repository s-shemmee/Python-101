*In this lesson, we go through the Python code that you just ran in the last lesson line by line to understand what it does. You'll be introduced to Python syntax, how to store data in variables as well as how to print out information to the screen.*

# Reading the Python Code Step by Step 

*Here's a step-by-step breakdown of our Python code.* 

## 1. Top of the file

```py
import random
```

*This imports other code. A library called 'random' that later allows us to pick out a random bar or random person from our lists.*

## 2. Lists of Bars & People 

```py
bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]

people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Kanye West",
          "Samuel L. Jackson"]
```

*These are lists of bars and people. They are going to be pulled into...*

## 3. Pick a random bar and a random person

```py
random_bar = random.choice(bars)
random_person_one = random.choice(people)

```

*This is where our script picks a random bar and a random person.*

## 4. Print out the results

```py
print(f"How about you go to {random_bar} with {random_person_one}
```

*This line prints out the random bar and random person.*
