## Introduction to Conditional Statements in Python

*Conditional statements (also known as if/than statements) let you define specific times when something should happen. For example,"if" you say yes "than" I'll tell you a joke. Or on a website, "if" you are logged into the site, "than" I will send you a special announcement. In this lesson, I'll show you how to write conditionals in Python.*

- Create a new file
- Create a new file called if.py:

answer = input("Do you want to hear a joke? ")

if answer == "Yes":
    print("I'm against picketing, but I don't know how to show it.")
    # Mitch Hedberg (RIP)
Running the file, we see our joke, or we don't. 

$ python if.py
Do you want to hear a joke? Yes
I'm against picketing, but I don't know how to show it.
$ python if.py
Do you want to hear a joke? No
$ 
How does == work in Python?
== checks to see whether two things are equal. It returns True if they are and False if they aren't.

$ python
>>> "Yes" == "Yes"
True
>>> "No" == "Yes"
False
Remember that even though they look similar, = and == are very different.

$ python
>>> answer = "Yes"
>>> answer == "Yes"
True
>>> answer = "No"
>>> answer == "Yes"
False
You can also use != to check if two things are different:

>>> answer != "Blue"
True
>>> answer != "No"
False
How does if work?
if will check to see if something is True and then run any indented code after (after the colon). 

if True:
    # Anything here will run
And accordingly: 

if False:
    # This will never run
