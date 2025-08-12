
class SumSolution:
    
    def compute(self, x, y):
        
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Not an int")

        if not (0 <= x <= 100) or not (0 <= y <= 100):
            raise ValueError("Not between 0 and 100")
        
        return x+y
