# Initialize list
myList = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
# Sort list in ascending order
myListAux = sorted(myList)

# Print sorted list
print(myListAux)

# Print sorted list in descending order
print(myListAux[::-1])

# Print even numbers from the list
print(myListAux[1:10:2])

# Print uneven number from list
print(myListAux[0:9:2])

# Print numbers that are multiples of 3
for i in myListAux:
    if myListAux[i-1] % 3 == 0:
        print(myListAux[i-1])
