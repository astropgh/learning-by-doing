"""
get_top_names.py
For astrophg/learning-by-doing: Task 7
https://github.com/astropgh/learning-by-doing/tree/master/task-07
"""

import pandas as pd
import numpy as np

def extract_data_lines(filename, start_text, end_text,
                       include_start=False, include_end=False):
    """
    open `filename`, and yield the lines between
    the line that contains `start_text` and the line that contains `end_text`
    """
    to_yield = False
    with open(filename) as fh:
        for line in fh:
            if end_text in line:
                if include_end:
                    yield line
                break
            if include_start == False:
                if to_yield:
                    yield line
            if start_text in line:
                to_yield = True
            if include_start:
                if to_yield:
                    yield line


if __name__ == '__main__':
    filename = '../task-03/top5names.html'
    start_text = '<tr><td align="center">2017</td>'
    end_text = '</table></center></div><!-- end #content -->'

    records = []
    data_lines = extract_data_lines(filename, start_text,
                                    end_text, include_start=True)

    readyear = True  # flag for reading line of years

    for line in data_lines:
        if readyear&('<tr><td align="center">' in line):
            year = int(line.replace('<tr><td align="center">', '').replace('</td>\n', ''))
            readyear = False
        elif '<tr><td align="center">' not in line:
            line_10_names = line.replace('</td> <td>', ' ').replace("<td>", " ").replace("</td></tr>\n", " ").split()
            for idx, name in enumerate(line_10_names):
                gender = 'female' if idx < 5 else 'male'
                rank = idx + 1 if idx < 5 else idx % 5 + 1
                records.append((year, gender, rank, name))
            readyear = True

    data = pd.DataFrame.from_records(records,
                                     columns=['year', 'gender', 'rank', 'name'])

    # Add your code for Step 3 here
    # You will use `data` to find and print out the answers for each questions listed in Task 4

    print('Q1: Which years Emma is the most chosen names?')
    print(data.query('name == "Emma"').query('rank == 1')['year'].tolist())
    print('\n')


    print('Q2:Which name had been the most chosen name for the longest consecutive years?')


    print('\n')


    print('Q3:How many unique male names have been on top 5 between years 1980 and 2000?')
    name_male = np.array(data.query('gender == "male"').query('year >= 1980').query('year <= 2000')['name'].tolist())
    print(len(np.unique(name_male)))
    print('\n')


    print('Q4:Are there more unique male names or more unique female names that are on top 5?')
    n_male = len(np.unique(np.array(data.query('gender == "male"')['name'].tolist())))
    n_female = len(np.unique(np.array(data.query('gender == "female"')['name'].tolist())))
    if n_female > n_male: print('There are more unique female names.')
    elif n_male > n_female: print('There are more unique male names.')
    else: print('There are equal unique names for female and male.')
    print('\n')


    print('Q5:What is the distribution of the numbers of consecutive years that a male name remains the most chosen name?')
    name_males = np.unique(np.array(data.query('gender == "male"')['name'].tolist()))
    # years_name = [data.query('name == "{}"'.format(name))['year'].tolist() for name in name_males]
    print('\n')
