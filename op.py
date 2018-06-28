import glob
marker = '::::::'
for name in glob.iglob("*.py"):
    inp = open(name, 'r', encoding='cp949')
    print(marker + name)
    print(inp.read())


