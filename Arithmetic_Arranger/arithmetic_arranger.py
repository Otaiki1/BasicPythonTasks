def arithmetic_arranger(problems, arithmetic_operation = False):
    
    arranged_problems = ""
    segments = []
    all_numbers = []
    tab = " " * 4
    #below code ensures there arent too many problems
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems
    
    #below code creates two lists , one forms a list for each value, the other for only numbers
    for i in range(len(problems)):
        segments = problems[i].split()
        all_numbers.extend([segments[0],segments[2]])
        
    #below code ensures the operators are either    
    operations = list(map(lambda x: x.split()[1], problems))
    for elements in operations:
        if elements != "+" :
            if elements != "-" :
                arranged_problems = "Error: Operator must be '+' or '-'."
                return arranged_problems
        
    for i in range(len(all_numbers)):
        if not all_numbers[i].isdigit() :
            arranged_problems = "Error: Numbers must only contain digits."
            return arranged_problems
        
        if len(all_numbers[i]) > 4 :
            arranged_problems = "Error: Numbers cannot be more than four digits."
            return arranged_problems
            
    top_row = ""
    bottom_row = ""
    dashes = ""
    values = ""
    value = "  "
    
    for i in range(len(problems)):
        segments = problems[i].split()
        length = max(len(segments[0]), len(segments[2])) 
        top = "  " +segments[0].rjust(length)
        bottom = segments[1] + " " + segments[2].rjust(length)
        result = str(eval(problems[i])) 
        length = length + 2
        dash = "-" * length
        value = str(result).rjust(length)
        if problems[i] != problems[-1]:
            top_row += top + tab      
            bottom_row  += bottom + tab 
            dashes += dash+ tab
            values += value + tab
        else:
            top_row += top      
            bottom_row  += bottom  
            dashes += dash
            values += value
    
    if arithmetic_operation :
        arranged_problems = '\n'.join((top_row, bottom_row, dashes, values))
    else:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes))
    return arranged_problems


        
            
