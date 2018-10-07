"""
get_top_names.py
For astrophg/learning-by-doing: Task 3
https://github.com/astropgh/learning-by-doing/tree/master/task-03
"""

def extract_data_lines(filename, start_text, end_text):
    """
    open `filename`, and yield the lines between
    the line that contains `start_text` and the line that contains `end_text`
    """
    turn_on = False
    with open(filename) as fh:
        for i,line in enumerate(fh):
            if turn_on=='done': break

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
    filename = 'top5names.html'
    start_text = '<tr><td align="center">2017</td>'
    end_text = '</table></center></div><!-- end #content -->'

    for line in extract_data_lines(filename, start_text, end_text):
        print(line)
