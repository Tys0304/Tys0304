message = "Hello, World!"

print(message)

first_character = message[0]
print("The first character is:", first_character)

length = len(message)
print("The length of the string is:", length)

name = input("Enter your name: ")

greeting = "Hello, " + name + "!"
print(greeting)


uppercase_message = greeting.upper()
print("Uppercase message:", uppercase_message)

contains_DuniA = "DuniA" in greeting
print("Does the message contain 'DuniA'? ", contains_DuniA)

new_message = message.replace("DuniA", "World")
print("Updated message:", new_message) 