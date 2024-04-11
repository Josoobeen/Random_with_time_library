import time

class Random():
  def __init__(self):
      self.t = int(str(time.time()).replace(".", ""))
      while len(str(self.t)) < 14:
          self.t = self.t ** 2
    
  def randint(self, a, b, c = 1):
      out = []
      while len(out) != c:
        x = range(a, b)
        self.t = self.t ** 2
        self.t = int(str(self.t)[:28])
        self.t = int(str(self.t)[:14]) + int(str(self.t)[14:28])
        y = self.t % len(x)
        out.append(x[y])

      if c == 1:
        return out[0]

      else:
        return out



"""
This place is for test
"""

import numpy as np
import matplotlib.pyplot as plt

target = 100
out = np.zeros(target)
random = Random()
for _ in range(1000000):
  out[random.randint(0, target)] += 1

plt.plot(out)
plot.show

