# Logic Operators

*In this lesson, we look at Python logical operators. The most popular ones you need to know are: `and`, `or` ,` not`, `==`, `!=`, `>`, and `<`. You'll also learn how to determine if a value is either True or False.*

*The most popular truth terms in Python are: `and`, `or` , `not`, `==`, `!=`, `>`, and `<`.*

*There's also `in`, which is a way of putting strings or variables together. As in:*

```bash
$ python
>>> people = ["Mattan", "Chris", "Sarah"]
>>> "Mattan" in people
True
```

## How Does the "or" Operator Work in Python?

*In this lesson, we introduce the "or" logical operator. This operator returns True if at least one of the expressions it's evaluating return True, otherwise, it returns False. You will learn some rules regarding the order in which it evaluates expressions—knowing this could save you from some logical bugs in your code.*

**The "or" operator**

- In `if.py`: 

```py
answer = input("Do you want to hear a joke? ")

if answer == "Yes" or answer == "yes":
    print("I'm against picketing, but I don't know how to show it.")
    # Mitch Hedberg (RIP)
elif answer == "No" or answer == "no" :
    print("Fine.")
else:
    print("I don't understand.")
```

## Understanding "in" in Python

*If you have several values and want to evaluate if a certain value is equal to any of the available values, you can either string together several comparison expressions with OR statements, or even better, you can place the values in a Python sequence—for instance, a list—and use the IN operator to check if your data is in the list. This makes the code succinct and more readable.*

**The "in" operator**

*So how do you cover all the different ways that a user could respond to an input? Well, you can put together a list, and then use in to pull responses from that list:*

In the `if.py` type:

```py
answer = input("Do you want to hear a joke? ")

affirmative_responses = ["yes", "y"]
negative_responses = ["no", "n"]

if answer.lower() in affirmative_responses:
    print("I'm against picketing, but I don't know how to show it.")
    # Mitch Hedburg (RIP)
elif answer.lower() in negative_responses:
    print("Fine.")
else:
    print("I don't understand.")

```

## Boolean Practice Challenge

*Time to put your newfound knowledge of Python logical operators to the test. In this lesson, you will download a .py (Python) file containing a list of conditional tests that evaluate to either True or False.*

Time for some [Boolean Practice](https://github.com/s-shemmee/Python-in-30-Days/blob/main/Projects/Logical_Operators/boolean_practice.py)!

## Boolean Practice Solutions

*Did you work through the last challenge? If you didn't, we recommend you go back and work through it before proceeding. Practicing is the best way to learn coding (or anything else). If you worked through the challenge, watch this lesson for the solutions to each of the problems and see how you did!*

Here's the full set of answers for our boolean logic problems. [Boolean Answers](https://github.com/s-shemmee/Python-in-30-Days/blob/main/Projects/Logical_Operators/boolean_practice_solutions.py)