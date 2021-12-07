import re
n = int(input())
string = ''
for _ in range(n):
    string += input()
pattern = re.compile(
    r'<a\shref="\s*?((https?://|//?)(www.)?[a-zA-Z0-9_./-;()%,:+?&=]+)\s*?".*?</')
matches = pattern.finditer(string)
for match in matches:
    print(match.group(1), end=',')
    w = match.span()
    s = string[w[0]:w[1]].strip()
    r = w[1] - 3
    res = ''
    while r:
        if string[r] == '>':
            break
        else:
            res += string[r]
            r -= 1
    print(res[::-1])
