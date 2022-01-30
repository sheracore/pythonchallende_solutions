import operator

class DoubleCal():

    def calculate(self, list_, relate):
        result = list()
        next_ = self.next
        for value in list_:
            next_ = relate(next_, value)
            result.append(next_ + self.initial)
            
        return(result)
