#! /usr/bin/python3

class DT:
    def __init__(self, attribute, boundary, left=None, right=None):
        self.attribute = attribute
        self.boundary = boundary
        if left:
           self.left = left 
        else:
           self.left = No()
        if right:
         self.right = right  
        else:
           self.right = Yes()  
        
    def check(self, sal):
        if sal[self.attribute] < self.boundary:
            return self.left.check(sal)
        else:
            return self.right.check(sal) 
            
class Yes():
   def __init__(self):
      pass
   def check(self, sal):
      return "Yes"
class No():
   def __init__(self):
      pass
   def check(self, sal):
      return "No"

midnight = DT("salary", 23000)
wfh = DT("wfh", 1, midnight)
tree = DT("salary", 25000, wfh)


print(tree.check({"salary": 15000, "wfh": 0, "midnight": 0}))