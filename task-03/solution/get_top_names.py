"""
get_top_names.py
For astrophg/learning-by-doing: Task 3
https://github.com/astropgh/learning-by-doing/tree/master/task-03
"""

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
    filename = '../top5names.html'
    start_text = '<tr><td align="center">2017</td>'
    end_text = '</table></center></div><!-- end #content -->'

    for line in extract_data_lines(filename, start_text, end_text, include_start=True):
        print(line)
