#! /usr/bin/python3

class DT:
    def __init__(self, attribute, boundary, left, right):
        self.attribute = attribute
        self.left = left 
        self.right = right
        self.boundary = boundary
        
        
    def check(self, jd_dict):
        if int(jd_dict[self.attribute]) < self.boundary: ##returns error "TypeError: 'int' object is not subscriptable"
            return False
        elif int(jd_dict[self.attribute]) >= self.boundary:
            if self.right:
                return self.right.check(jd_dict[self.attribute])
            else:
                return True

dt = DT('salary', 1000, False,
        DT('nightshift', 0, True, False))

ans = {
        'salary': 3000,
        'nightshift': 0,
    }

print(dt.check(ans))