"""
get_top_names.py
For astrophg/learning-by-doing: Task 7
https://github.com/astropgh/learning-by-doing/tree/master/task-07
"""

import pandas as pd
import re
from itertools import groupby

def extract_data_lines(filename, start_text, end_text, include_start=False, include_end=False):
    """
    open `filename`, and yield the lines between
    the line that contains `start_text` and the line that contains `end_text`
    """
    turn_on = False
    with open(filename) as fh:
        for i, line in enumerate(fh):
            if turn_on == 'done': break

            if end_text in line:
                if include_end:
                    turn_on = 'done'
                    yield line
                break

            if turn_on: yield line

            if start_text in line:
                if include_start:
                    turn_on = True
                    yield line
                turn_on = True


if __name__ == '__main__':
    filename = '../task-03/top5names.html'
    start_text = '<tr><td align="center">2017</td>'
    end_text = '</table></center></div><!-- end #content -->'

    records = []
    data_lines = extract_data_lines(filename, start_text, end_text, include_start=True)
    for data_line in data_lines:

    genders = {i:'Female' if i<5 else 'Male' for i in range(10)}
    for line in extract_data_lines(filename, start_text, end_text, include_start=True, include_end=False):
            line = re.split(' |align="center"|<td|>|<td>|<tr>|</td>|</tr>|\n', line)
            line = list(filter(None, line))
            if len(line)==1:
                year = int(line[0])
            else:
                for i, name in enumerate(line):
                    records.append((year, genders[i], i%5+1, name))

    data = pd.DataFrame.from_records(records, columns=['year', 'gender', 'rank', 'name'])

    # Add your code for Step 3 here
    # You will use `data` to find and print out the answers for each questions listed in Task 4

    # For example, to answer question 1 Which years Emma is the most chosen names?:
    print(data.query('name == "Emma"').query('rank == 1')['year'].tolist())

    # question 2 Which name had been the most chosen name for the longest consecutive years?
    for gender in ["Male", "Female"]:
        df1 = df.query('gender == "'+str(gender)+'"').query('rank == 1')['name'].tolist()
        print(gender+' name with most occurences is ',
            sorted([(name, sum(1 for _ in occurence)) for name, occurence in groupby(df2)], key=lambda x: x[1])[:-1][0][0])
    # question 3 How many unique male names have be on top 5 between years 1980 and 2000?
    print(len(set(df[np.logical_and.reduce((df['gender']=='Male', df['rank']<=6 , df['year']>=1980, df['year']<=2000))]['name'])))

    # question 4 Are there more unique male names or more unique female names that are on top 5? prints True if more unique male names
    print(len(set(df[np.logical_and(df['gender']=='Male', df['rank']<=5)]['name']))/len(set(df[np.logical_and(df['gender']=='Female', df['rank']<=5)]['name']))>1)

    # question 5 What is the distribution of the numbers of consecutive years that a male name remains the most chosen name?
    df2 = df.query('gender == "Male"').query('rank == 1')['name'].tolist()
    np.histogram([(sum(1 for _ in occurence)) for _, occurence in groupby(df2)])
