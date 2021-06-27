from collections import Counter


def repeatedString(s, n):
    dic = Counter(s)
    countA = dic['a']
    numberOfRepetitions = n // len(s)
    elemLeft = n - (numberOfRepetitions * len(s))
    extraDic = Counter(s[:elemLeft])
    extraA = extraDic['a']
    return (countA * numberOfRepetitions) + extraA
