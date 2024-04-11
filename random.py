import time

class Random():
    def __init__(self):
        self.t = int(str(time.time()).replace(".", ""))
        while len(str(self.t)) < 14:
            self.t = self.t ** 2
    
    def randint(self, a, b, c = 1, duplicate = True):
        """
        Randint between a and b.
        if c is 1, return 1 integer data.
        if c is over 1, return list data.
        """
        if type(a) is not int or type(b) is not int or type(c) is not int:
            raise "a, b, c must be integer"
        elif a > b:
            raise "b must be bigger than a"
        elif c < 1:
            raise "c must be bigger than 1"
        elif duplicate == False:
            if b - a + 1 < c:
                raise "c must be bigger than b - a"
                
        
        out = []
        while len(out) != c:
            x = range(a, b + 1)
            self.t = self.t ** 2
            self.t = int(str(self.t)[:28])
            self.t = int(str(self.t)[:14]) + int(str(self.t)[14:28])
            y = self.t % len(x)
            if duplicate == False:
                if x[y] in out:
                    continue
                else:
                    out.append(x[y])
            else:
                out.append(x[y])
            
        if c==1:
            return out[0]
        else:
            return out
        
    def choice(self, a):
        """
        a is list.
        """
        return a[self.randint(0, len(a)-1)]
    
    def choices(self, a, b):
        """
        a is list.
        b is amount you need.
        In this code, same data inside a can be out.
        """
        if type(a) is not list and type(a) is not tuple:
            raise "a must be list or tuple"
        elif type(b) is not int:
            raise "b must be integer"
        elif b < 1:
            raise "b must be bigger than 0"
        elif len(a) < 1:
            raise "a need more than 1 data in container"
        
        out = []
        b = self.randint(0, len(a)-1, b)
        out += [a[i] for i in b]
        
        return out
    
    def sample(self, a, b):
        """
        a is list.
        b is amount you need.
        In this code, same data inside a can be out.
        """
        if type(a) is not list and type(a) is not tuple:
            raise "a must be list or tuple"
        elif type(b) is not int:
            raise "b must be integer"
        elif b < 1:
            raise "b must be bigger than 0"
        elif len(a) < 1:
            raise "a need more than 1 data in container"
        elif len(a) < b:
            raise "a has no enough data inside container"
        
        c = self.randint(0, len(a)-1, c = b, duplicate = False)
        out = [a[i] for i in c]
        
        return list(out)
        
      






"""
This place is for test
"""

import numpy as np
import matplotlib.pyplot as plt

target = 100
out = np.zeros(target+1)
random = Random()
for _ in range(1000000):
    out[random.randint(0, target)] += 1

plt.plot(out)
plot.show
