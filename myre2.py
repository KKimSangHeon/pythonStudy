import re
from sys import stdin

data = """kim 920312-1065411
          lee 934121-1089811"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split("\n"):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit*():
            word = word[:6] + "-" + "*******"
            word_result.append(word)
        result.append("".join(word_result))
    print("\n".join(result))


pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******",data))

p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)

pattern = 'this'
text = "Does this text match the pattern?"

match = re.search(pattern, text)

s = match.start()
e = match.end()

print('found %s\n in %s \n from %d to %d %s' % (match.re.pattern, match.string, s, e , text[s:e]))

text =''
