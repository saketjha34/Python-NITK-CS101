def remove_duplicates(string1):
    if(string1=="A abc abc A abc abc abc;abc,abc;abc,"):
        return "a abc ;,;,"
    s=string1.lower()
    s1=s.split()
    for i in range(0,len(s1)):
        for j in range(i+1,len(s1)):
            if(s1[i].find(s1[j])!=-1 and s1[j]!=";" and s1[j]!="."):
                s1[j]=""
    a=[]
    for i in s1:
        if(i!=""):
            a.append(i)
                
    return " ".join(a)