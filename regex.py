
import re
re.findall(r"\bf[a-z]*","which foot or hand fell fastest");

li = re.findall(r"01\d*-\d*-\d*",
           """031-737-7924, 8451051, 010-2962-5042,
           3:17 heewook 011-2516-6514 017-337-2924""")
print ([i[:-1] for i in li])
