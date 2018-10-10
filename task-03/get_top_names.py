#"""
#get_top_names.py
#For astrophg/learning-by-doing: Task 3
#https://github.com/astropgh/learning-by-doing/tree/master/task-03
#"""

def extract_data_lines(filename, start_text, end_text, include_start = False, include_end = False):
    """
    open `filename`, and yield the lines between
    the line that contains `start_text` and the line that contains `end_text`
    """

    # Needed to record the text in between
    parsing = False
    
    # use `yield line` to return desired lines but keep the function going
    with open(filename) as fh:
        
        for line in fh:
                       
            ######################################################################
            
            if start_text in line:
                
                parsing = True
                
                if not include_start:
                    
                    continue
                    
            ######################################################################     
                
            elif end_text in line:
                
                if include_end:
                    
                        #parsing = True
                        yield line
                        break
                        
                else:
                        
                        parsing = False
                
            ######################################################################
                
                
            if parsing: # Do stuff with the data
                
                yield line
                        


if __name__ == '__main__':
    filename = 'top5names.html'
    start_text = '<tr><td align="center">2017</td>'
    end_text = '</table></center></div><!-- end #content -->'
    

    for line in extract_data_lines(filename, start_text, end_text, include_start = False, include_end = False):
        
            print(line)