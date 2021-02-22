"""
get_top_names.py
For astrophg/learning-by-doing: Task 3
https://github.com/astropgh/learning-by-doing/tree/master/task-03
"""

def extract_data_lines(
    filename,
    start_text,
    end_text,
    include_start=False,
    include_end=False,
):
    """
    open `filename`, and yield the lines between
    the line that contains `start_text` and the line that contains `end_text`
    """
    # fill in code as needed
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
    filename = 'top5names.html'
    start_text = '<tr><td align="center">2017</td>'
    end_text = '</table></center></div><!-- end #content -->'
    include_start = False
    include_end = False

    args = (
        filename,
        start_text,
        end_text,
        include_start,
        include_end
    )

    for line in extract_data_lines(*args):
        print(line)
