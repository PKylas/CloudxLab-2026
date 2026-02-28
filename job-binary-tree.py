#! /usr/bin/python3

class DT:
    def __init__(self, jd_dict, attribute, boundary, left, right):
        self.jd_dict = jd_dict
        self.attribute = attribute
        self.left = left 
        self.right = right
        self.boundary = boundary
        
        
    def check(self, jd_dict):
        if jd_dict[self.attribute] < self.boundary: #check salary
            return "No"
        elif jd_dict[self.attribute] >= self.boundary:
            if self.right:
                return self.right.check(jd_dict[self.attribute]) #does not check nightshift
            else:
                return "Yes"

jd_dict = {'salary': 3000, 'nightshift': 0}
instance = DT(jd_dict, attribute="salary", boundary=1000, left=None, right=None) #Only one key can be given as the attribute
print(instance.check(jd_dict))