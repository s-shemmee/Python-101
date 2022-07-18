# Python <img src="https://media.giphy.com/media/LMt9638dO8dftAjtco/giphy.gif" alt="cover" width="50"/>

# What is Python and why it is used?

*Python is a general-purpose programming language that has wide application in various fields. In this documentation, we look at some areas in which Python is used, for example in web development, desktop app development, data science, building Internet of Things, creating distributed systems, etc.*

*What can you do with Python? There are many, many cool things! We take a look, as well as cover what you will learn in this documentation.*

# Features of Python

## Cross-platform

*Python can be worked on multiple platforms such as Windows, Linux, etc.*

## Open Source

*The reference implementation of Python i.e. CPython is Open Source.*

## Multiple Programming-paradigms

*Programming Paradigms classify programming languages based on features, such as functional, procedural, object-oriented, declarative, etc. Python supports multiple programming paradigms such as object-oriented, functional programming, imperative, etc.*

## Fewer lines of code

*A Python program uses lesser lines of code than C, C++, or Java, which makes it simpler*

# How Should I Start Learning Python?

*You might be wondering: How and why should I start learning Python? To help you answer that, we’ll look at various programming languages and compare a few popular ones with Python.*

- So I'll give you three examples in PHP, Python, and Ruby.

 > Php

```php
echo "Hello World";
```

> Python

```python
print ("Hello World")
```

> Ruby

```ruby
puts "Hello World"
```

*Now if I run this code the end result I get is the text Hello World.*

*So the outcome is exactly the same but the way that it looks is a little different like you might have noticed that the PHP has a semicolon at the end, that Python has that parenthesis around the Hello World, Ruby doesn't have either of those but the end result is exactly the same.*

*You'll find out why Python is a useful tool to have under your belt whether you are learning your first language or looking to learn an additional one. You’ll find out why Python is especially a good language to learn for first-time developers.*

# Python 2 vs Python 3

*Python was created in 1991 by Guido Van Rossum. Guido is known as the Benevolent Dictator for Life because he is so awesome.*
*And it's actually named after Monty Python, not the snake, as, you know, some people erroneously believe.*

*Python 2 is legacy, Python 3 is the future and so we recommend learning the latter. The two versions share similarities, so if you learn Python 3, you will still be able to read and understand any legacy Python 2 code you might come upon.*

*We look at the history of Python and explore the differences between Python 2 and Python 3. For the course, we use (and recommend) Python 3.* 


# Setup and Basic Python

## Installing Python and Setting Up Your Development Environment (IDE)

*Before you can start coding with Python, you have to ensure that your computer is set up right. I'll take you through the process of installing Python on your MacOS, Windows or Linux OS via the Anaconda distribution. After that, you'll need to install a code editor. I use vs code and would suggest it for this course. But you can use any text editor you prefer.*

## Can We Take A Sanity Check?

*"How do I know which version of Python I have?" is one of the most common questions I hear from students. In this section, I'll show you how to verify that you set up your development environment right. You'll test your Python installation and ensure that you have the right version of Python installed—version 3.0 or later*.

**1. Install Vs Code**

*Before we write our first line of Python code, you'll need to install a text editor (sometimes called an IDE). In this course, we'll be using vs code.*

- Step 1 :

  - Download VS code from here <a href="https://code.visualstudio.com/download">Link</a>.

- Step 2 :

  - Download the Visual Studio Code installer for Windows. Once it is downloaded, run the installer (VSCodeUserSetup-{version}.exe). Then, run the file – it will only take a minute.

  <img src="https://www.educative.io/api/edpresso/shot/5485113345835008/image/6359130978123776"/>

  - Accept the agreement and click `“next”`.

  <img src="https://www.educative.io/api/edpresso/shot/5485113345835008/image/5970797106036736"/>

  - After accepting all the requests press finish button. By default, VS Code installs under: `"C:\users{username}\AppData\Local\Programs\Microsoft VS Code."`

<img src="https://www.educative.io/api/edpresso/shot/5485113345835008/image/6505951994052608">

  - If the installation is successful, you will see the following:

  <img src="https://www.educative.io/api/edpresso/shot/5485113345835008/image/4587054357282816">


**2. Install Python**

*To download Python, go to <a href="https://www.python.org">Python’s official website</a>.*

*Now, keep the mouse cursor on the Downloads menu. The current version of Python i.e. Python 3.10 can now be seen,*

<img src="https://studyopedia.com/wp-content/uploads/2020/10/1.-Download-Python-3.9.png"/>

*On clicking, the download begins,*

<img src="https://studyopedia.com/wp-content/uploads/2020/10/2.-Python-3.9-downloading-begins.png">

*After the download completes, click on the arrow, and select Open to begin installing,*

<img src="https://studyopedia.com/wp-content/uploads/2020/10/3.-Start-installing-Python-3.9.png">

*Installation steps initiated. Select the checkbox `“Add Python 3.9 to PATH“`. After that, click Customize Installation as shown below:*

<img src="https://studyopedia.com/wp-content/uploads/2020/10/4.-Python-3.9-installation-started.png">

*Now, you will reach the section Optional Features. This by default checks the “pip” package installer, test suite, py launcher, etc. Pip is used to install and manage Python packages.*

*Keep the default and click `“Next“`:*

<img src="https://studyopedia.com/wp-content/uploads/2020/10/5.-Python-installation-test-suite-pip-py-lancher-settings.png">

*The Advanced Options section would be visible now. Select Install for all users. On selecting it will set the following installation path on its own. You can change the installation path by clicking Browse. If you want to keep the default path, click Install,*

<img src="https://studyopedia.com/wp-content/uploads/2020/10/6.-Set-Python-installation-path.png">

*Installation of all the components begins,*

<img src="https://studyopedia.com/wp-content/uploads/2020/10/7.-Python-components-installing.png">

*After a few seconds, the installation completes as shown below. Click Close,*

<img src="https://studyopedia.com/wp-content/uploads/2020/10/8.-Python-3.9-setup-completes.png">

**3. Set Up Your Command Line**

*The command line is where you run your code once you've written it, and its already installed by default on most computers.*

*Now, verify whether we have successfully installed Python or not.*

*Go to `START` -> type `CMD`, right-click `Open as Administrator`.*

<img src="https://studyopedia.com/wp-content/uploads/2020/10/9.-Open-CMD-to-verify-Python-installation.png">

*The Command Prompt opens as shown below,*

<img src="https://studyopedia.com/wp-content/uploads/2020/10/10.-CMD-opens.png">

*Now, on typing the following command python –version on CMD, the following is visible, that means Python successfully installed on our Windows 10 OS:*

<img src="https://studyopedia.com/wp-content/uploads/2020/10/11.-Python-3.9-successfully-installed-on-Windows-10.png">


**Common Issues Installing Python**

- Make sure you restart your computer after running the Python installer.

- Make sure you only type python in the prompt (no quotes, no spaces, no punctuation, nothing).

- You may have to disable antivirus temporarily.

- If you're on a work computer and it doesn't let you install Python or Sublime Text then you may need to contact your IT team and request permission.

# Python Variables: How to Define/Declare String Variable Types

## What is a Variable in Python?

*A Python variable is a reserved memory location to store values. In other words, a variable in a python program gives data to the computer for processing.*

## Python Variable Types

*Every value in Python has a datatype. Different data types in Python are Numbers, List, Tuple, Strings, Dictionary, etc. Variables in Python can be declared by any name or even alphabets like a, aa, abc, etc.*

*In this tutorial, we will learn,*

- How to Declare and use a Variable
- Re-declare a Variable
- Concatenate Variables
- Local & Global Variables
- Delete a variable

## How to Declare and use a Variable

*Let see an example. We will define variable in Python and declare it as `“a”` and print it.*

```py
a = 100 
print (a)
```

> Output

```py
100
```

## Re-declare a Variable

*You can re-declare Python variables even after you have declared once.*

*Here we have Python declare variable initialized to a=0.*

*Later, we re-assign the variable a to value “shemmee”*

```py
# Declare a variable and initialize it
a = 0

# Re-declaring the variable works

a = 'shemmee'

```

> Output

```py
0
shemmee
```

> Python 2 Example

```py
# Declare a variable and initialize it
f = 0
print f
# re-declaring the variable works
f = 'shemmee'
print f
```

> Python 3 Example

```py
# Declare a variable and initialize it
f = 0
print(f)
# re-declaring the variable works
f = 'shemmee'
print(f)
```

## Python String Concatenation and Variable

*Let’s see whether you can concatenate different data types like string and number together. For example, we will concatenate “shemmee” with the number “21”.*

*Unlike Java, which concatenates number with string without declaring number as string, while declaring variables in Python requires declaring the number as string otherwise it will show a TypeError*

- For the following code, you will get undefined output

```py
a = "shemmee"
b = 21
print a+b
```

- Once the integer is declared as string, it can concatenate both `“shemmee”` + `str(“21”)`= `“shemmee21”` in the output.

```py
a="shemmee"
b = 21
print(a+str(b))
```

## Python Variable Types: Local & Global

*There are two types of variables in Python, Global variable and Local variable. When you want to use the same variable for rest of your program or module you declare it as a global variable, while if you want to use the variable in a specific function or method, you use a local variable while Python variable declaration.*

*Let’s understand this Python variable types with the difference between local and global variables in the below program.*

- Let us define variable in Python where the variable “f” is global in scope and is assigned value 101 which is printed in output

- Variable f is again declared in function and assumes local scope. It is assigned value “I am learning Python.” which is printed out as an output. This Python declare variable is different from the global variable “f” defined earlier

- Once the function call is over, the local variable f is destroyed. At line 12, when we again, print the value of “f” is it displays the value of global variable f=101

```py
# Declare a variable and initialize it aka Global variable
f = 101
print(f)

# Local variable in function
def someFunction();
  f = 'i am learning Python'
  print(f)

someFunction()

print(f)
```
> Output:

```py
101
i am learning Python
101
```

*While Python variable declaration using the keyword **global**, you can reference the global variable inside a function.*

- Variable “f” is **global** in scope and is assigned value 101 which is printed in output

- Variable f is declared using the keyword **global**. This is **NOT** a **local variable**, but the same **global** variable declared earlier. Hence when we print its value, the output is 101

- We changed the value of “f” inside the function. Once the function call is over, the changed value of the variable “f” persists. At line 12, when we again, print the value of “f” is it displays the value “changing global variable”

> Example

```py
f = 101;
print (f)
# Global vs.local variables in functions
def someFunction():
  global f
  print (f)
  f = "changing global variable"
someFunction()
print (f)
```

> Output:

```py
101
101
changing  global variable
```

## Delete a variable

*You can also delete Python variables using the command del `“variable name”`.*

*In the below example of Python delete variable, we deleted variable f, and when we proceed to print it, we get error **“variable name is not defined”** which means you have deleted the variable.*

```py
f = 11;
print(f)
del f
print(f)
```

## Summary:

- Variables are referred to “envelop” or “buckets” where information can be maintained and referenced. Like any other programming language Python also uses a variable to store the information.
- Variables can be declared by any name or even alphabets like a, aa, abc, etc.
- Variables can be re-declared even after you have declared them for once
- Python constants can be understood as types of variables that hold the value which can not be changed. Usually Python constants are referenced from other files. Python define constant is declared in a new or separate file which contains functions, modules, etc.
- Types of variables in Python or Python variable types : Local & Global
- Declare local variable when you want to use it for current function
- Declare Global variable when you want to use the same variable for rest of the program
- To delete a variable, it uses keyword “del”.
