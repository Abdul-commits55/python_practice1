# Step 1 – Ask for user details
name = input("What is your name? ")
age = int(input("How old are you? "))  # Convert to integer
fruits = input("Enter your 3 favourite car: ")

# Step 2 – Split fruits into a list
fruit_list = fruits.split(",")

# Step 3 – Use string functions
print(f"\nGood Afternoon, {name}")          # Greeting with f-string
print("Your name in uppercase:", name.upper())  # Uppercase name
print("Length of your name:", len(name))        # Length of name

# Display results
print("\n--- User Information ---")
print("Name:", name)
print("Age:", age)
print("Favourite car:", fruit_list)
