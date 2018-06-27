import random

q = random.randrange(100)
while(1):
    a = int(input("input 1~99 "))
    if a == q:
        print("right")
        break
    elif a < q:
        print("up")
    else:
        print("down")