# Ask for user details
name = input("What is your name: ")
age = int(input("How old are you: "))  # Convert to integer
fruits = input("Enter your 3 favourite fruits: ")

# Split fruits into a list
fruit_list = fruits.split(",")

# Display results
print("\n--- User Information ---")
print("Name:", name)
print("Age:", age)
print("Favourite Fruits:", fruit_list)