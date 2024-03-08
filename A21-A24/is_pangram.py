def is_pangram(sentence):

    sentence = sentence.lower()
    set1 = set()
    for i in sentence:
        if 'a' <= i <= 'z':
            set1.add(i)
    
    return len(set1) == 26
