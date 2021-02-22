#!/Users/troyraen/anaconda/bin/python
"""
get_top_names.py
For astrophg/learning-by-doing: Task 7
https://github.com/astropgh/learning-by-doing/tree/master/task-07
"""

import pandas as pd
import numpy as np

def extract_data_lines(filename, start_text, end_text, include_start=False, include_end=False):
    # Add your code for Step 1 here
    # Just copy your answer from task-03
    # Remove the raise statement when you are done
    trgr = False
    with open(filename) as fh:
        for line in fh:
            # print(line)
            if trgr:
                if end_text in line:
                    trgr = False
                    if include_end:
                        yield line
                else:
                    yield line
            else:
                if start_text in line:
                    trgr = True
                    if include_start:
                        yield line
    # raise NotImplementedError


if __name__ == '__main__':
    filename = './task-03/top5names.html'
    start_text = '<tr><td align="center">2017</td>'
    end_text = '</table></center></div><!-- end #content -->'

    records = []
    data_lines = extract_data_lines(filename, start_text, end_text, include_start=True)

    # Add your code for Step 2 here
    # This will involve a for loop that iterates over `data_lines`
    # For each row, you will append a tuple to `records`
    gdic = {1:'Female', 2:'Male'}
    for ln in data_lines:
        # print(ln[0:5])
        if 'align' in ln:
            yr = ln.strip('<tr><td align="center"> </td>\n')
        else:
            names = ln.strip('<td> </td></tr>\n').split('</td> <td>')
            if len(names) != 10:
                print("there are not 10 names!")

            for g in [1,2]:
                for i in range(5):
                    j = i if g==1 else i+5
                    records.append((yr, gdic[g], i, names[j]))

        # data.query('rank==1').iterrows() (pandas?)
        # pd.value_counts

    data = pd.DataFrame.from_records(records, columns=['year', 'gender', 'rank', 'name'])
    # print(data.sample(5))

    # Add your code for Step 3 here
    # You will use `data` to find and print out the answers for each questions listed in Task 4
    sdata = [ data[data['gender']=='Female'], data[data['gender']=='Male'] ]
    fdata, mdata = sdata

    # For example, to answer question 1:
    print()
    print("Emma was the number one female name in")
    print(data.query('name == "Emma"').query('rank == 1')['year'].tolist())

    # top consecutive names
    for d in sdata:
        prev_name = 'none'
        count=0
        top = ['name',0]
        g = d.iloc[-1].gender
        for __, row in (d.query('rank == 1').sort_values('year')).iterrows():
            if row['name'] == prev_name:
                count = count+1
            else:
                if count > top[1]:
                    top = [prev_name, count]
                prev_name = row['name']
                # print(prev_name)
                count = 0
        print()
        print('Top consecutive', g, 'name was', top[0], 'for', top[1], 'years.')


    # unique names
    lm = len(set(mdata.query('year > "1979"').query('year < "2001"')['name']))
    print()
    print('There were', lm, 'unique male names in the top 5 between 1980 and 2000')
    # print(mdata.query('year > "1979"'))

    lm = len(set(mdata['name']))
    lf = len(set(fdata['name']))
    g = 1 if lf > lm else 2
    print()
    print('There are more unique', gdic[g], 'names in the top 5 for all years.')


    # distribution of top consecutive names
    for d in [mdata]:
        prev_name = 'none'
        count=0
        numc = []
        g = d.iloc[-1].gender
        for __, row in (d.query('rank == 1').sort_values('year')).iterrows():
            if row['name'] == prev_name:
                count = count+1
            else:
                numc.append(count)
                prev_name = row['name']
                # print(prev_name)
                count = 0
        numa = np.asarray(numc)
        # print(numc)
        print()
        print('Number of consecutive years that the same male name was on top, number of times this happened')
        for i in range(numa.max()+1):
            tot = len(np.where(numa==i)[0])
            print(i, ', ', tot)
