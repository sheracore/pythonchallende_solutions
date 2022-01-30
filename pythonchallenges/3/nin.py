import operator

from ten import DoubleCal

class DoubleMul(DoubleCal):

    def __init__(self, initial=0):
        self.initial = initial
        self.next = 1


obj = DoubleMul()
list_ = [3,4,6,2,1,9,0,5,7,8]
    
print(list_)
print("\n8 : ",obj.calculate(list_, max))
