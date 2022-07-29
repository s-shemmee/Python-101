# Python Print() Statement: How to Print with Examples

In this tutorial, you will learn

- How to Print a simple String in Python?
- How to print blank lines
- Print end command

## Python print() function

*The print() function in Python is used to print a specified message on the screen. The print command in Python prints strings or objects which are converted to a string while printing on a screen.*

Syntax:

```py
print(object(s))
```

## How to Print a simple String in Python?

*More often then not you require to Print strings in your coding construct.*

*Here is how to print statement in Python 3:*

> Example: 1

*To print the Welcome to Guru99, use the Python print statement as follows:*

```py
print ("Welcome to s-shemmee's Github")
```

> Output:

```py
Welcome to s-shemmee's Github
```

*In Python 2, same example will look like*

```py
print "Welcome to s-shemmee's Github"
```

>Example 2:

If you want to print the name of five countries, you can write:

```py
print("USA")
print("Canada")
print("Germany")
print("France")
print("Japan")
```

> Output:

```py
USA
Canada
Germany
France
Japan
```
## How to print blank lines

*Sometimes you need to print one blank line in your Python program. Following is an example to perform this task using Python print format.*

> Example:

*Let us print 8 blank lines. You can type:*

```py
print (8 * "\n")
```

*or:*

```py
print ("\n\n\n\n\n\n\n\n\n")
```

> Here is the code

```py
print ("Welcome to s-shemmee's Github")
print (8 * "\n")
print ("Welcome to s-shemmee's Github")
```

> Output

```
Welcome to s-shemmee's Github







Welcome to s-shemmee's Github
```

## Print end command

*By default, print function in Python ends with a newline. This function comes with a parameter called ‘end.’ The default value of this parameter is ‘\n,’ i.e., the new line character. You can end a print statement with any character or string using this parameter. This is available in only in Python 3+*

> Example 1:

```py
print ("Welcome to", end = ' ') 
print ("s-shemmee's Github", end = '!')
```

> Output:

```
Welcome to s-shemmee's Github!
```

> Example 2:

`#` ends the output with `@`.

```py
print("Python" , end = '@')
```

> Output:

```py
Python@
```