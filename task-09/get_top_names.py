"""
get_top_names.py
For astrophg/learning-by-doing: Task 9
https://github.com/astropgh/learning-by-doing/tree/master/task-09
"""

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


class NameRecorder:
    def __init__(self):
        self.records = []
        self.year = None

    def add(self, name, is_female, rank):
        if self.year is None:
            raise ValueError('One must set year first')

        # complete this member function
        raise NotImplementedError

    def to_pandas(self):
        # complete this member function
        raise NotImplementedError

    def clear(self):
        self.records.clear()
        self.year = None


if __name__ == '__main__':
    filename = '../task-03/top5names.html'
    start_text = '<tr><td align="center">2017</td>'
    end_text = '</table></center></div><!-- end #content -->'

    data_lines = extract_data_lines(filename, start_text, end_text, include_start=True)

    recorder = NameRecorder()
    for i, data_line in enumerate(data_lines):
        if i % 2:
            names = data_line.replace('<td>', ' ').replace('</td>', ' ').replace('</tr>', ' ').strip().split()
            for j, name in enumerate(names):
                recorder.add(name, is_female=(j < 5), rank=(j % 5 + 1))
        else:
            recorder.year = int(data_line.replace('<tr><td align="center">', '').strip()[:4])

    data = recorder.to_pandas()

    print(data.query('name == "Emma"').query('rank == 1')['year'].tolist())
