class Bag:
    def __init__(self):
        self.data = []

    def add(self,x):
        self.data.append(x)

    def __add__(self, x):
        self.data.append(x)

    def __sub__(self, x):
        if x in self.data: self.data.remove(x)

    def __mul__(self, x):
        self.data *= x

    def __repr__(self):
        return "This is Bag"

    def addtwice(self, x):
        self.add(x)
        self.add(x)


l = Bag( )
l.add('first')
l.addtwice('second')
print(l.data)


l+"third"
print(l.data)

l-"third"
print(l.data)

l*3
print(l.data)