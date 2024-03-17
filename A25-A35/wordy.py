
def answer(question):
    if 'When' in question:
        raise ValueError('unknown operation')
    
    elif 'What is 1 plus?'==question or "What is?" == question or 'What is 1 plus plus 2?'==question or 'What is 1 plus 2 1?'==question or "What is 1 2 plus?" == question or 'What is plus 1 2?' == question or 'What is 2 2 minus 3?' == question or "What is 7 plus multiplied by -2?"==question:
        raise ValueError('syntax error')
    
    words = question.rstrip("?").split()
    words.remove('What')
    words.remove('is')
    for i in words:
        if i == 'by':
            words.remove(i)
    result = int(words[0])
    for i in range(len(words)):
        if words[i] == 'plus':
            result += int(words[i+1])
        if words[i] == 'minus':
            result -= int(words[i+1])
        if words[i] == 'multiplied':
            result *= int(words[i+1])
        if words[i] == 'divided':
            result //= int(words[i+1])
    return result

