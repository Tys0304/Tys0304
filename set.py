fruits = {"apple", "banana", "cherry", "date"}

fruits.add("grape")

fruits.remove("cherry")

contains_banana = "banana" in fruits
contains_orange = "orange" in fruits

print("Fruits:")
for fruit in fruits:
    print(fruit)

citrus_fruits = {"orange", "lemon", "lime"}

union_fruits_citrus = fruits.union(citrus_fruits)
intersection_fruits_citrus = fruits.intersection(citrus_fruits)
difference_fruits_citrus = fruits.difference(citrus_fruits)

print("Contains 'banana'? ", contains_banana)
print("Contains 'orange'? ", contains_orange)
print("Union of fruits and citrus fruits:", union_fruits_citrus)
print("Intersection of fruits and citrus fruits:", intersection_fruits_citrus)
print("Difference between fruits and citrus fruits:", difference_fruits_citrus)