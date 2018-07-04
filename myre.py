import re
from sys import stdin

pat = re.compile(r'[-\w][-.\w]*@[-\w][-\w.]+[a-zA-Z]{2,4}]')

found = set()

for line in stdin.readlines():
    for address in pat.findall(line):
        found.add(address)

for address in sorted(found):
    print(address)
