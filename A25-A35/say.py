div_10 = (
                "zero",
                "one",
                "two",
                "three",
                "four",
                "five",
                "six",
                "seven",
                "eight",
                "nine",
                "ten",
                "eleven",
                "twelve",
                "thirteen",
                "fourteen",
                "fifteen",
                "sixteen",
                "seventeen",
                "eighteen",
                "nineteen",
                 )
div_100 = (
            "zero",
            "ten",
            "twenty",
            "thirty",
            "forty",
            "fifty",
            "sixty",
            "seventy",
            "eighty",
            "ninety")


def say(number):
    if  number < 0 or number > 999999999999:
        raise ValueError("input out of range")
    if number < 20:
        return div_10[number]
    elif number < 100:
        tens = int(number/10)
        rest = number%10
        return div_100[tens] + ("-" + say(rest) if rest > 0 else "")
    elif number < 1000:
        hundrets = int(number/100)
        rest = number%100
        return div_10[hundrets] + " hundred" + (" " + say(rest) if rest > 0 else "")
    elif number < 1000000:
        thousands = int(number/1000)
        rest = number%1000
        return say(thousands) + " thousand" + (" " +say(rest) if rest > 0 else "")
    elif number < 1000000000:
        million = int(number/1000000)
        rest = number%1000000
        return say(million) + " million" + (" "+ say(rest) if rest > 0 else "")
    elif number < 1000000000000:
        billion = int(number/1000000000)
        rest = number%1000000000
        return say(billion) + " billion" + (" "+ say(rest) if rest > 0 else "")
  
