#! /usr/bin/python3

dict_terms = {}

str = input("Please enter a sentence: ").split()

for item in str:
    dict_terms[item] = dict_terms.get(item, 0)+1

print(dict_terms)