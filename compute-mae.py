#! /usr/bin/python3


def compute_mae(LA, LP):
    sum = i = j = 0
    counter=0
    for i in range(len(LA)):
        j = 0
        for j in range(len(LA[i])):
            n = abs(LA[i][j]-LP[i][j])
            sum += n
    length = len(LA)*len(LA[i])
    return (sum/length)

        
dim = int(input("Please enter the number of rows for data: "))
list_of_actual = []
list_of_predicted = []

for i in range(dim):
    row = input(f"Actual data: Please enter numbers separated by a blank space for row {i}: ")
    actual = list(map(int, row.split()))
    list_of_actual.append(actual)


for i in range(dim):
    row = input(f"Predicted data: Please enter numbers separated by a blank space for row {i}:")
    predicted = list(map(int, row.split()))
    list_of_predicted.append(predicted)

mae = 0
mae = compute_mae(list_of_actual, list_of_predicted)
print("The Mean Absolute Error is:", mae)



