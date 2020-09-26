# Using bubble sort which is inefficient.
# If sorting algorithm can be improved it will be much efficient

def ssb(arr):                                                                      
    N = len(arr)                                                                   
    for i in range(N):                                                             
        for j in range(i+1, N):                                                    
            if comparator(arr[i], arr[j]):                                         
                arr[i], arr[j] = arr[j], arr[i]                                    
    return "".join(arr)                                                            
                                                                                   
                                                                                   
                                                                                   
def comparator(x, y):                                                              
    if x + y > y + x:                                                              
        return True                                                                
    else:                                                                          
        return False                                                               
                                                                                   
                                                                                   
print(ssb(["a","bd","ac","cd"]))                                              
print(ssb(["c","cc","cca","cccb"]))
