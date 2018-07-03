import re
from sys import stdin

pat = re.compile(r'[-\w][-.\w]*@[-\w][-\w.]+[a-zA-Z]{2,4}]')

for line in stdin.readlines():
    for address in pat.findall(line):
        print(address)
