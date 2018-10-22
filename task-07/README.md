# Task 7: Data scraping

*prerequisites*: [Task 3](../task-03), [Task 4](../task-04)

Finally, we will now actually do the data scraping!

The data model we will use for this task would be
a table with 4 columns: year, gender, rank, name.
Each row in this table corresponds to one cell that contains one name
in the original table on the website.

Each year will result in 10 rows. The first two rows of this table would look like:

| year | gender | rank | name |
| ---- |--------| -----| ---- |
| 2017 | female | 1 | Emma |
| 2017 | female | 2 | Olivia |


## Steps

*(Do Step 1-3 in `task-07/get_top_names.py`)*

1. Copy the answer from Task 3 to complete the function `extract_data_lines`
2. Complete the data scraping: add a for loop that iterates over `data_lines` and
   append a tuple to `records` for each name (corresponds to each row in the new table).
3. Use the table we constructed (stored as a pandas data frame to answer the questions in Task 4.)
4. Submit a pull request for your solution.

## Food for thought:
- Do you think this is a good data model? Why or why not?
- What assumptions did you make when you implement Step 2?
  How likely will your scraping method fail if the underlying webpage source changes?
