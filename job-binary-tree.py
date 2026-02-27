#! /usr/bin/python3

class DT:
    def __init__(self, attribute, boundary, left, right):
        self.attribute = attribute
        self.left = left 
        self.right = right
        self.boundary = boundary
        
        
    def check(self, jd_dict):
        if jd_dict[self.attribute] < self.boundary:
            return self.left.check()
        else:
            return self.right.check()

No = DT()
Yes = DT()

dt = DT('salary', 1000, No, 
        DT('nightshift', 1, No, Yes))

ans = dt.check(
    {
        'salary': 3000,
        'nightshift': 0,
    })

print(ans)