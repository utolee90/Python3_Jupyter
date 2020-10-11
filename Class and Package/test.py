
class Test:
    def __init__(self, _num):
        self.num = _num
    
    def show(self):
        print(self.num)
    
    def plus(self):
        self.num += 1
    
    def minus(self):
        self.num -= 1

def sumarg(*args): 
    return sum(args)