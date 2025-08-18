name = input("What is your name: ")
age = int(input("How old are you: "))
fruits = input("Enter your 3 favourite fruits : ")

fruit_list = [fruit.strip() for fruit in fruits.split(",")]

print(f"\nGood Afternoon, {name}")
print("Your name in uppercase:", name.upper())
print("Length of your name:", len(name))

print("\nFirst fruit:", fruit_list[0])
print("Last fruit:", fruit_list[-1])

new_fruit = input("Enter one more fruit to add: ")
fruit_list.append(new_fruit.strip())

print("Updated fruit list:", fruit_list)

print("\n--- User Information ---")
print("Name:", name)
print("Age:", age)
print("Favourite Fruits:", fruit_list)
