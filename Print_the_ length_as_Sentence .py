num_char = len(input("Whats your name?"))

# print("Your name has "+ num_char+ "characters")
#~~~ This in its current form will give you an error as num_char is an int and not a string. To fix this, we need to convert it to a string.

# Correct method would be:
print("Your name has " + str(num_char) + " Characters")

