# Python TUPLE – Pack, Unpack, Compare, Slicing, Delete, Key

## What is Tuple Matching in Python?

**Tuple Matching in Python** *is a method of grouping the tuples by matching the second element in the tuples. It is achieved by using a dictionary by checking the second element in each tuple in python programming. However, we can make new tuples by taking portions of existing tuples.*

- Tuple Syntax

```py
Tup = ('Jan','feb','march')
```

- To write an empty tuple, you need to write as two parentheses containing nothing-

```
tup1 = ();
```

- For writing tuple for a single value, you need to include a comma, even though there is a single value. Also at the end you need to write semicolon as shown below.

```py
Tup1 = (50,);
```

- Tuple indices begin at 0, and they can be concatenated, sliced and so on.

> In this tutorial, we will learn

- Packing and Unpacking
- Comparing tuples
- Using tuples as keys in dictionaries
- Deleting Tuples
- Slicing of Tuple
- Built-in functions with Tuple
- Advantages of tuple over list

**Tuple Assignment**

*Python has tuple assignment feature which enables you to assign more than one variable at a time. In here, we have assigned tuple 1 with the persons information like name, surname, birth year, etc. and another tuple 2 with the values in it like number (1,2,3,….,7).*

>For Example:

(name, surname, birth year, favorite movie and year, profession, birthplace) = Robert

```py
tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida');
tup2 = (1,2,3,4,5,6,7);
print(tup1[0])
print(tup2[1:4])
```

