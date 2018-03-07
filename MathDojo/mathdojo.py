class MathDojo(object):
    def __init__(self):
        self.result = 0
    
    def add(self,*args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for n in i:
                    self.result += n
            else:
                self.result += i
        return self

    def subtract(self,*args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for n in i:
                    self.result -= n
            else:
                self.result -= i
        return self
            
   

    

    

md = MathDojo()

print md.add(2).add(2,5).subtract(3,2).result
print md.add([1], 3,4).add([3,5,7,8], [2,4,3,5]).subtract(2, [2,3], [1,5]).result


