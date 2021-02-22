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

    # '<tr><td align="center">2017</td>\n'
    # '<td>Emma</td> <td>Olivia</td> <td>Ava</td> <td>Isabella</td> <td>Sophia</td> <td>Liam</td> <td>Noah</td> <td>William</td> <td>James</td> <td>Logan</td></tr>\n'

    for line in data_lines:
        if 'align="center"' in line:
            year = int(line.strip().split('<tr><td align="center">')[1].split('</td>')[0])
        else:
            names = [it.split('</td>')[0] for it in line.strip().split('<td>')[1:]]
            for ii, name in enumerate(names):
                rank = (ii % 5) + 1
                gender = 'female' if ii < 5 else 'male'
                records.append((year, gender, rank, name))

    data = pd.DataFrame.from_records(records, columns=['year', 'gender', 'rank', 'name'])

    # Add your code for Step 3 here
    # You will use `data` to find and print out the answers for each questions listed in Task 4

    # For example, to answer question 1:
    # 1. Which years Emma is the most chosen names?
    print(data.query('name == "Emma"').query('rank == 1')['year'].tolist())
    print(data.query('name == "Emma" and rank == 1')['year'].tolist())

    # 2. Which name had been the most chosen name for the longest consecutive years?
    male = {'previous': '', 'cnt': 0, 'runs': []}
    female = {'previous': '', 'cnt': 0, 'runs': []}
    for __, it in data.query('rank == 1').iterrows():
        dd = male if it.gender == 'male' else female
        if it['name'] == dd['previous']:
            dd['cnt'] += 1
        else:
            if dd['previous'] != '':
                dd['runs'].append((dd['previous'], dd['cnt']))
            dd['cnt'] = 1
            dd['previous'] = it['name']

    runs = pd.DataFrame(male['runs'] + female['runs'], columns=['name', 'cnt'])
    print('Name with the longest run at the top:', runs.name[runs.cnt.idxmax()])

    # 3. How many unique male names have be on top 5 between years 1980 and 2000?
    print(len(set(data.query('year >= 1980 and year <= 2000 and gender == "male"')['name'])))

    # 4. Are there more unique male names or more unique female names that are on top 5?
    unique_male_names = len(set(data.query('gender == "male"')['name']))
    unique_female_names = len(set(data.query('gender == "female"')['name']))

    if unique_male_names > unique_female_names:
        print('More unique male names.')
    elif unique_male_names < unique_female_names:
        print('More unique female names.')
    else:
        print('Same number of unique male and female names.')

    # 5. What is the distribution of the numbers of consecutive years that a male name remains the most chosen name?
    previous = ''
    count = 0
    runs = []
    for it in data.query('gender == "male" and rank == 1')['name']:
        if it == previous:
            count += 1
        else:
            if previous != '':
                runs.append(count)
            count = 1
            previous = it

    print('Distribution:\n', pd.value_counts(runs))
