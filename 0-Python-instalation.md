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