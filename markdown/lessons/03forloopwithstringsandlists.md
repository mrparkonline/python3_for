---
title: ""
draft: false
weight:
lesson: true
descriptor: ""
---

# For Loop with Strings and Lists
---

### Index based iteration with Strings and Lists

Both strings and lists are indexable, so we can access individual items by indicitaing an index with square brackets.

__Examples:__


```python
print('Hello'[1]) # Should output letter 'e' at index of 1
```

    e



```python
print(['Apple', 'Bananas', 'Kiwi', 'Strawberry'][2]) # Kiwi!
```

    Kiwi


_Let's see some examples with for loops_


```python
# Using a for loop on a string with index
# NOTE: programmers often use single letters when creating an iterating variable
# I like to use i as "index"

phrase = 'Hello, World!'
size = len(phrase)

for i in range(size):
    print('Current character at index', i, 'is:', phrase[i])
```

    Current character at index 0 is: H
    Current character at index 1 is: e
    Current character at index 2 is: l
    Current character at index 3 is: l
    Current character at index 4 is: o
    Current character at index 5 is: ,
    Current character at index 6 is:  
    Current character at index 7 is: W
    Current character at index 8 is: o
    Current character at index 9 is: r
    Current character at index 10 is: l
    Current character at index 11 is: d
    Current character at index 12 is: !



```python
# Using for loop on a list of fruits via index

fruits = ['Apple', 'Banana', 'Kiwi', 'Strawberry']

print('The fruits in my blender:')

for i in range(len(fruits)):
    print('    --', fruits[i])
```

    The fruits in my blender:
        -- Apple
        -- Banana
        -- Kiwi
        -- Strawberry


__NOTE:__
- recall that ```range()``` never includes the last value
- indexing in Python always starts at __0__(zero).
- Therefore, a string of: ```Hello``` has its last character at index of 4, but has a length of 5
- Same idea applies to lists as well.


### Accessing items in a String or a List without indexing

We can also just iterate through strings or lists by using a for loop without the need for the index values.

__Examples:__


```python
# For loop on string

phrase = 'Hello, World!'

for character in phrase:
    print('Current Character:', character)
```

    Current Character: H
    Current Character: e
    Current Character: l
    Current Character: l
    Current Character: o
    Current Character: ,
    Current Character:  
    Current Character: W
    Current Character: o
    Current Character: r
    Current Character: l
    Current Character: d
    Current Character: !



```python
# For loop on list

fruits = ['Apple', 'Banana', 'Kiwi', 'Strawberry']

for fruit in fruits:
    print('Current fruit:', fruit)
```

    Current fruit: Apple
    Current fruit: Banana
    Current fruit: Kiwi
    Current fruit: Strawberry

