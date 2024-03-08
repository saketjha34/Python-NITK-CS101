'''Compare Lists'''

def compare_lists(a_list, b_list):
   
    for i in range(len(a_list)):
        bool = False
        for j in b_list:
            if j < 0:
                raise ValueError("Wrong output")

            if a_list[i]**2 == j:
                bool = True
        if not bool:
            return False  
    
    return True    


