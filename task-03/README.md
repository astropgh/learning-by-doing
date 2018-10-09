# Task 3: [algorithm] Preparing for data scraping

This task is to prepare for a later task that we will do a simple data scraping,
in which we will parse the data from a webpage.

This task asks you to complete a function that reads in a file, goes through it
line-by-line, and only *yields* the lines we need, specified by the contents of
the starting line and ending line.

The starting line and ending line are known. You should only pass through the
file **once**.


## Steps

1. Complete the generator function `extract_data_lines` in `get_top_names.py`
2. Submit a pull request for your solution.


## Extension

Does your function yield the starting line and ending line themselves, or just the lines in between? 
What if we want to have the options to include the starting/ending lines? 
Can you add two optional arguments `include_start` and `include_end` to `extract_data_lines` to 
control its behavior? 


## Background

The `yield` statement in Python turns a regular function to a generator,
which can be used like an iterable. For example, running the following code

```python
def iterate_abc():
    for x in 'abc':
        yield x.upper()

for y in iterate_abc():
    print(y)
```
will result in
```
A
B
C
```
