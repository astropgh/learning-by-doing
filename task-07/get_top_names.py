"""
get_top_names.py
For astrophg/learning-by-doing: Task 7
https://github.com/astropgh/learning-by-doing/tree/master/task-07
"""

import pandas as pd


def extract_data_lines(filename, start_text, end_text, include_start=False, include_end=False):
    """
    open `filename`, and yield the lines between
    the line that contains `start_text` and the line that contains `end_text`
    """
    # Add your code for Step 1 here
    # Just copy your answer from task-03
    # Remove the raise statement when you are done

    with open(filename) as fh:
        in_table = False
        for line in fh:

            if start_text in line:
                in_table = True
                if not include_start:
                    continue

            elif end_text in line:
                if include_end:
                    yield line
                break

            if in_table:
                yield line


if __name__ == '__main__':
    filename = '../task-03/top5names.html'
    start_text = '<tr><td align="center">2017</td>'
    end_text = '</table></center></div><!-- end #content -->'

    records = []
    data_lines = extract_data_lines(filename, start_text, end_text, include_start=True)

    # Add your code for Step 2 here
    # This will involve a for loop that iterates over `data_lines`
    # For each row, you will append a tuple to `records`

    data = pd.DataFrame.from_records(records, columns=['year', 'gender', 'rank', 'name'])

    # Add your code for Step 3 here
    # You will use `data` to find and print out the answers for each questions listed in Task 4

    # For example, to answer question 1:
    print(data.query('name == "Emma"').query('rank == 1')['year'].tolist())
