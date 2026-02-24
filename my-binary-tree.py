#! /usr/bin/python3

class Node:
    left = None
    right = None
    def __init__(self, val):
        self.val = val
    def printa(self):
        if self.left:
            self.left.printa()
        print(self.val)
        if self.right:
            self.right.printa()
    def search(self, value): # True or false
        if value < self.val:
            if self.left:
                return self.left.search(value)
            else:
                return False
        elif value == self.val:
            return True
        else:
            if value > self.val:
               if self.right:
                 return self.right.search(value)
               else:
                return False
    def insert(self, value):
        if value < self.val:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = Node(value)         
        else:
            if value > self.val:
                if self.right:
                    return self.right.insert(value)
                else:
                    self.right = Node(value)


root = Node(10)
root.left = Node(5)
root.left.left = Node(1)
root.left.right = Node(7)
root.right = Node(16)
root.right.left = Node(12)
root.printa()
a = 21
print(f"Is {a} present in the binary tree?", root.search(a))
if root.search(a) is False:
    print(f"Let's insert {a}.")
root.insert(a)
root.printa()