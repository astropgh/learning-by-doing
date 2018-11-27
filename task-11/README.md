# Task 11: Safeguard your algorithm (Exception handling)

*prerequisites*: [Task 7](../task-07), [Task 9](../task-09)

In [Task 7](../task-07) where we did data scraping, one of the
food-for-thought questions is what assumptions you have made about the raw data
when you write the scraping code.

If the structure of the top name website source code (i.e., the raw data) has
now changed a bit, your original script may not work as intended. In this case,
if you just run the original script, the script may raise an error that may not
be informative, or the script may run but result in unexpected result.

If the script is an important component in your project, or it runs periodically,
then you would probably like to save your future self some time when debugging it.
A good practice here is to safeguard your code by doing exception handling.
That is, you expect what error/exception may happen, and, instead of just let the
code breaks or continues to run with the wrong data, you catch the error/exception
and provide meaningful hints for your future self.

Luckily, Python provides excellent infrastructure for exception handling.
If you have never heard of the try-except statement or the raise statement,
you can search for the keywords "Python Exceptions" on the Internet, or look at
[this tutorial](https://docs.python.org/3/tutorial/errors.html) (particularly
relevant are Sec 8.3 and 8.4).


## Steps

This is a simple task. Look at the code snippet we introduce in [Task 9](../task-09),
reproduced below. Add some code as suggested so that when the format of the
underlying raw data (website source) change, you code will raise an Exception with
meaningful message.

```python
recorder = NameRecorder()
for i, data_line in enumerate(data_lines):
    if i % 2:
        names = data_line.replace('<td>', ' ').replace('</td>', ' ').replace('</tr>', ' ').strip().split()
        # add some code here to conduct a check.
        # if the check fails, and raise an RuntimeError with meaningful message
        for j, name in enumerate(names):
            recorder.add(name, is_female=(j < 5), rank=(j % 5 + 1))
    else:
        try:
            recorder.year = int(data_line.replace('<tr><td align="center">', '').strip()[:4])]
        # finish the try-except statement to conduct a check.
        # if the check fails, raise an RuntimeError with meaningful message
data = recorder.to_pandas()
```
