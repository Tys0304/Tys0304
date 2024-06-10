numbers = [1, 2, 3, 4, 5]

print("Original list:", numbers)

first_element = numbers[0]
print("The first element is:", first_element)


subset = numbers[2:4]
print("Subset of the list:", subset)


numbers[1] = 10
print("Modified list:", numbers)



numbers.append(6)
print("List after appending 6:", numbers)

numbers.remove(3)
print("List after removing 3:", numbers)


index_of_4 = numbers.index(4)
print("Index of 4:", index_of_4)

contains_7 = 7 in numbers
print("Does the list contain 7?", contains_7)

numbers.sort()
print("Sorted list:", numbers)

numbers.reverse()
print("Reversed list:", numbers)

 
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])