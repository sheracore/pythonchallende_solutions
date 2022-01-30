import operator

from ten import DoubleCal

class DoubleSum(DoubleCal):

    def __init__(self, initial=0):
        self.initial = initial
        self.next = 0


obj = DoubleSum(initial=100)
list_ = [1,2,3,4,5]

print(list_)
print("\n7 : ",obj.calculate(list_, operator.add))
