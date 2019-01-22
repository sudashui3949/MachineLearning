class A():
    def __enter__(self):
        self.a=1
        return self
    def f(self):
        print 'f'
    def __exit__(self,a,b,c):
        print 'exit'
def func():
    return A()

with A() as a:
    a.f()
    print a.a
