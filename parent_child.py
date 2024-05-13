class A:
    def f(self):
        print("class A")

class B(A):
    def h(self):
        print("class B")

class C(B):
    def x(self):
        print("Class c")

obj=C()
obj.h()
obj.f()
obj.x()