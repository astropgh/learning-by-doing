"""
get_top_names.py
For astrophg/learning-by-doing: Task 7
https://github.com/astropgh/learning-by-doing/tree/master/task-07
"""

from collections import Counter
import numpy as np
import pandas as pd

def extract_data_lines(filename, start_text, end_text, include_start=False,
                       include_end=False):
    """
    open `filename`, and yield the lines between
    the line that contains `start_text` and the line that contains `end_text`.
    """
    started = False
    with open(filename) as fh:
        for line in fh:
            if started:
                if end_text in line:
                    if include_end:
                        yield line
                    break
                yield line
            elif start_text in line:
                started = True
                if include_start:
                    yield line


if __name__ == '__main__':
    filename = '../../task-03/top5names.html'
    start_text = '<tr><td align="center">2017</td>'
    end_text = '</table></center></div><!-- end #content -->'

    records = []
    data_lines = extract_data_lines(filename, start_text, end_text, include_start=True)

    year = None
    for i, data_line in enumerate(data_lines):
        if i % 2:
            names = data_line.replace('<td>', ' ').replace('</td>', ' ').replace('</tr>', ' ').strip().split()
            for j, name in enumerate(names):
                records.append((year, 'female' if j < 5 else 'male', j % 5 + 1, name))
        else:
            year = int(data_line.replace('<tr><td align="center">', '').strip()[:4])

    data = pd.DataFrame.from_records(records, columns=['year', 'gender', 'rank', 'name'])

    # Add your code for Step 3 here
    # You will use `data` to find and print out the answers for each questions listed in Task 4

    # Question 1:
    print(data.query('name == "Emma"').query('rank == 1')['year'].tolist())

    # Question 2 (and 5):
    longest_consecutive_name = None
    longest_consecutive_year = 0
    for gender in ('female', 'male'):
        names = data.query('rank == 1').query('gender == "{}"'.format(gender))['name'].values
        name_change_idx = np.flatnonzero(np.hstack(([True], names[1:] != names[:-1], [True])))
        years = np.ediff1d(name_change_idx)
        for years_this, idx in zip(years, name_change_idx[1:]):
            if years_this > longest_consecutive_year:
                longest_consecutive_name = names[idx-1]
                longest_consecutive_year = years_this
    consecutive_years_dist_male = Counter(years) # store this for question 5
    print(longest_consecutive_name) # print out answer for question 2

    # Question 3:
    n_unique_male_1980_2000 = len(set(data.query('gender == "male"').query('year >= 1980').query('year <= 2000')['name']))
    print(n_unique_male_1980_2000)

    # Question 4:
    n_unique = {}
    for gender in ('female', 'male'):
        n_unique[gender] = len(set(data.query('gender == "{}"'.format(gender))['name']))
    if n_unique['female'] > n_unique['male']:
        print('More unique female top names')
    elif n_unique['female'] < n_unique['male']:
        print('More unique male top names')
    else:
        print('Same number of unique female and male top names')

    # Question 5 (print out only):
    print(consecutive_years_dist_male)
