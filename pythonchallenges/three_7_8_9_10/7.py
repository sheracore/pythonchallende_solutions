class DoubleSum():

    def __init__(self, initial=0):
        self.initial = initial

    def calculate(self, list_):
        print(list_)
        result = list()
        next_ = 0
        for value in list_:
            next_ += value
            result.append(next_ + self.initial)

        return(result)


obj = DoubleSum(initial=100)
list_ = [1,2,3,4,5]
print(obj.double_sum(list_))
