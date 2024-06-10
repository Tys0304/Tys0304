fruits = ("apple", "banana", "cherry", "date")

( "a" , 1 , 2.3 , "b" )



first_fruit = fruits[0]
second_fruit = fruits[1]

print("Fruits:")
for fruit in fruits:
    print(fruit)

contains_cherry = "cherry" in fruits

num_fruits = len(fruits)

more_fruits = ("grape", "kiwi")
all_fruits = fruits + more_fruits

nested_tuple = ("red", ("green", "blue"))

print("First fruit:", first_fruit)
print("Second fruit:", second_fruit)
print("Does it contain 'cherry'? ", contains_cherry)
print("Number of fruits:", num_fruits)
print("All fruits:", all_fruits)
print("Nested tuple:", nested_tuple)