# Sequence-based Iteration: For Loop
---

### For Loop

Much like how a _while loop_ will repeat its own block of code, __For Loop__ will also repeat its own block of code.

For loops don't __depend on a conditional statement being True__. For loops will repeat a finite amount of time dependent on the size/length of the __iterating sequence__.

```python

# For Loop Format

for __iterating_variable__ in __iterating__sequence__:

    your code here

# end of for loop

```

- A for loop is started by using the keyword: ```for```
- ```__iterating_variable__``` is a label that you create to represent the individual items in the sequence
- No matter the iterating variable, __the code within the for loop will execute__
- The code within the for loop executes repeatedly until the iterating variable runs out of items to represent from the sequence

### What is a Sequence?

__Sequence__ is a collection of items or things.
- The sequence can be ordered(least to greatest) or unordered(shuffled)
- These sequences will have a beginning and an end; therefore, they are finite
- We can determine the size of the sequences

##### Examples:
- List of integers: ```[2,3,5,7,11,13]```
- A string: ```"Sequence"``` is a sequence of 8 characters
- In Python, a __data type__ that is classified as _iterable_ will be able to iterate within a for loop
    - Examples: Lists, Strings, Tuples
    
### Code Example #1


```python
# Using a for loop with a string
# Purpose: Output individual letters of a word.

word = 'Hello!'

for character in word:
    print('Current Character:', character)
```

    Current Character: H
    Current Character: e
    Current Character: l
    Current Character: l
    Current Character: o
    Current Character: !


__Explanation:__
- The label ```character``` is used as a label to represent each single item from the iterating sequence for each iteration
- The variable ```word``` is a string that has the characters: ```Hello!```
- Since ```character``` represents individual items, we were able to grab the items in the sequence in order and one-by-one

### Code Example #2


```python
# Using a for loop, but ignoring the iterating variable
# Purpose: Repeat a message

word = 'Hello!'

for character in word:
    print('Goodbye!')
```

    Goodbye!
    Goodbye!
    Goodbye!
    Goodbye!
    Goodbye!
    Goodbye!


__Explanation:__
- In Code Example 2, the iterating variable ```character``` is not used within the for loop's code block
- The string of ```Goodbye!``` is outputted 6 times.
- There are 6 outputs because variable: ```word``` has 6 items in the sequence
