class FourVector:
    def __init__(self, vector = [0,0,0,0]):
        self.vector = vector

    def __str__(self):
        return str(tuple(self.vector))
    
    def __round(self, num):
        if(type(num) == float):return round(num, 2)
        return num
    
    def GetComponents(self):
        return self.vector
    
    def SetComponents(self, vector):
        self.vector = vector
    
    def __add__(self, v2):
        n = []
        for i in range(len(self.vector)):
            op = self.__round(self.vector[i] + v2.GetComponents()[i]) 
            n.append(op)
        return FourVector(n)
    
    def __sub__(self, v2):
        n = []
        for i in range(len(self.vector)):
            op = self.__round(self.vector[i] - v2.GetComponents()[i]) 
            n.append(op)
        return FourVector(n)
    
    def __eq__(self, other):
        if isinstance(other, FourVector):
            return self.vector == other.vector
        return False

v1 = FourVector([1,2,3,4])
v2 = FourVector([4,8,2,0])

print(v1 - v2)
