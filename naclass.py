# 내가 self가 필요 없어도 자식은 self가 필요하다

class grandfather:
    def earnplay(self):
        print("thired")

class father(grandfather):
    def earnplay(self):
        print("money")

class uncle(grandfather):
    def earnplay(self):
        print("give money")

class na(father, uncle):
    def earnplay(self):
        print("game")

k = father()

print(isinstance(k, father))
print(isinstance(k, grandfather))

kk=na()
kk.earnplay()