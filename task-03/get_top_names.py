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
        include_end=False):
    """Open `filename`, and yield the lines between start and end text

    Args:
        filename       (str): Path of the file to open
        start_text     (str): Line in file to start yielding from
        end_text       (str): Line in file to stop yielding at
        include_start (bool): Whether to yield start_text (Default false)
        include_end   (bool): Whether to yield end_text (Default false)
    """

    with open(filename) as ofile:
        stop_iteration = False
        yield_content = False

        for line in ofile:
            if stop_iteration:
                raise StopIteration

            cleaned_line = line.strip()
            if start_text in cleaned_line:
                yield_content = True
                if include_start:
                    yield cleaned_line

            elif end_text in cleaned_line:
                stop_iteration = True
                if include_end:
                    yield cleaned_line

            elif yield_content:
                yield cleaned_line


if __name__ == '__main__':
    filename = 'top5names.html'
    start_text = '<tr><td align="center">2017</td>'
    end_text = '</table></center></div><!-- end #content -->'

    for line in extract_data_lines(filename, start_text, end_text, 0, 0):
        print(line)
