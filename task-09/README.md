# Task 9: Using a Python class

*prerequisites*: [Task 7](../task-07)

In this task, we will repeat Step 2 of Task [Task 7](../task-07), but this time
we utilize a Python class.

Look at the following code that does the data scraping step, you can notice that
by using this `recorder` object, we have made the code more readable.
Also, if we would like to change our data model in the future, we won't need to
change this part of the code, but only change how this `recorder` object works.

```python
recorder = NameRecorder()
for i, data_line in enumerate(data_lines):
    if i % 2:
        names = data_line.replace('<td>', ' ').replace('</td>', ' ').replace('</tr>', ' ').strip().split()
        for j, name in enumerate(names):
            recorder.add(name, is_female=(j < 5), rank=(j % 5 + 1))
    else:
        recorder.year = int(data_line.replace('<tr><td align="center">', '').strip()[:4])
data = recorder.to_pandas()
```

This user-facing code *define* how the `NameRecorder` would operate.
We will write this `NameRecorder` class that makes this code segment work.

## Steps

1. Complete the `NameRecorder` class in `task-09/get_top_names.py`.

2. (Optional) Add an `to_sql` member function that takes one argument `filename`,
   and writes out the table to a sqlite database.

## References

You can read more about Python classes at
https://github.com/astropgh/Hack-Hour/blob/master/Python%20Tutorials/01_classes.ipynb

## Food for thought

- What are other benefits of writing a class in this use case, compared to what
  we did in Task 7?
