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

*The best way to learn to code is by coding. In this lesson, you will dive into your first programming challenge. Don't be scared, let's dive in together! In the next lesson, we’ll review the solution (no peeking just yet).*

# Happy Hour Challenges

- I misspelled Samuel L Jackson's name. Fix the typo.
- Add another person to the list of people.
- Change the script so it prints out two random people instead of one. (ex. How about you go to Lion's Head Tavern with Mattan and Chris?)
