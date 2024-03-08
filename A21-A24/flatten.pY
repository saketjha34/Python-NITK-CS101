def flatten(list1):
    output_list=[]
    for i in list1:
        if type(i)==list:
            output_list.extend(flatten(i))
        elif i is not None:
            output_list.append(i)
    return output_list 

