
a = [99, "bottles of beer", ["on", "the", "wall"]]
a[0] = 98
a[1:2] = ["bottles", "of", "beer"]
del a[-1]
print(a)

a = list(range(5))
a.append(5)
a.pop()
a.insert(0, 42)
print(a.pop(0))

D = {"duck": "eend", "wtaer": "water"}
print(D.get("duck"))
print(D.get("back"))

a = [1,2,3]
b = a
b = a.append(4)
print(a)
# a = [1,2,3,4]

a = [1,2,3]
b = a
b = a[:]
print(a)
# a = [1,2,3]\

even = set([2, 4, 6, 8])
print(6 in even)
for e in even: print(e)

tel = {'Stef':62606, 'Mel':62663}
print(tel['Mel'])
print('Stef' in tel)
print(62663 in tel.values() )
for name in tel: print(name)

a = 42;
print(id(a))
b = a+1
a += 1
print(id(a))

for i in range(20):
    if i%3 == 0:
        print(i)
        if i%5 == 0:
            print ("Bingo!")
    print("---")


def output(text):
    print(text)


text = "outer"
print(text)
output("inner")
print(text)


def gcd(a, b):
    "greatest common divisor"
    while a != 0:
        a, b = b%a, a    #병렬 할당( parallel assignment)
    return b
print(gcd.__doc__)
print(gcd(12, 20))


def count_gc(sequence):
    """Counts the nitrogenous bases of the given sequence.
    Ambiguous bases are counted fractionally.
    Sequence must be in upper case"""
    gc = 0
    for base in sequence:
        if   base in 'GC':
            gc += 1.0
        elif base in 'YRWSKM':
            gc += 0.5
        elif base in 'DH':
            gc += 0.33
        elif base in 'VB':
            gc += 0.66
    return gc


def gc_content(sequence):
    """Calculates the GC content of a DNA sequence.
    Mixed case, gaps and ambiguity codes are permitted"""
    sequence = sequence.upper().replace('-',"")
    if not sequence:
        return 0
    return 100.0 * count_gc(sequence) / len(sequence)


print(gc_content("actacgattagag"))


class Stack:
    "A well-known data structure…"
    def __init__(self):		# 생성자와 유사한 역할
        self.items = []
    def push(self, x):
        self.items.append(x)	           # 추가하는 제한은???
    def pop(self):
        x = self.items[-1]		# 만약에 비어있다면 어떤 일이 발생???
        del self.items[-1]
        return x
    def empty(self):
        return len(self.items) == 0	# 참 또는 거짓을 반환
x = Stack()
print(x.empty())
print(x.push(1))
print(x.empty())
print(x.push("hello"))
print(x.pop())
print(x.items)
class FancyStack(Stack):
    "stack with added ability to inspect inferior stack items"

    def peek(self, n):
        "peek(0) returns top; peek(-1) returns item below that; etc."
        size = len(self.items)
        assert 0 <= n < size			# 조건을 이용한 사전 검사
        return self.items[size-1-n]


class LimitedStack(FancyStack):
    "fancy stack with limit on stack size"

    def __init__(self, limit):
        self.limit = limit
        FancyStack.__init__(self)		# 기초 클래스 생성자

    def push(self, x):
        assert len(self.items) < self.limit
        FancyStack.push(self, x)		# "조상" 함수 호출


x = LimitedStack(30)
print(x.empty())
print(x.push(1))
print(x.empty())
print(x.push("hello"))
print(x.pop())
print(x.items)


class Connection:
    verbose = 0				# 클래스 변수
    def __init__(self, host):
        self.host = host			# 인스턴스 변수
    def debug(self, v):
        self.verbose = v			# 인스턴스 변수 생성!
    def connect(self):
        if self.verbose:			# 이것은 인스턴스 변수인가? 클래스 변수인가?
            print("connecting to %r"%self.host)
c = Connection("192.168.105.25")
c.debug(True)
c.connect()


def foo(x):
    return 1/x

def bar(x):
    try:
        print(foo(x))
    except ZeroDivisionError as message:
        print("Can’t divide by zero:", message)

print(bar(0))
