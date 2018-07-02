class MyClass:
    "A simple example class"
    i = 123
    __a = 123   # 숨기는 변수가 된다.

    def f(self):
        return 'hello world'


print(MyClass().i)

