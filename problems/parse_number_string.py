def parse(strr):                                                                   
    # if no string then return 0
    if not strr:                                                                   
        return 0                                                                   
                             
    # Initialize variables
    sum = 0                                                                        
    q = []                                                                         
                                                                                   
    # if digit then put in list else if character then do the sum                                                                               
    for ch in strr:                                                                
        if is_number(ch):                                                          
            q.append(ch)                                                           
        else:                                                                      
            if q:                                                                  
                sum += int("".join(q))                           
                q.clear()      
                
    # In case list is not empty
    if q:                                                                          
        sum += int("".join(q))                                                     
    return sum                                                                     
                                                                                   
                                                                   
def is_number(num):                                                                
""" Function to check whether a character is a number or alphabet """
    try:                                                                           
        digit = int(num)                                                           
        if digit >=0 and digit<=9:                                                 
            return True                                                            
    except ValueError:                                                             
        return False                                                               
                                                                                   
print(parse("a1se23rt56789bn0987"))
