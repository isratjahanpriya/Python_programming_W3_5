print("Program starting.\n")
print(f"Options:\n1 - Celsius to Fahrenheit\n2 - Fahrenheit to Celsius\n0 - Exit")
print(f"Welcome to the unit converter program!\nFollow the menu instructions below.\n")
option=input("Your choice: ")
if option== "1":
    celsius = float(input("Insert the amount of Celsius: "))
    farenheit = celsius * 1.8 + 32
    farenheit = round(farenheit, 1)
    print(f"{celsius} °C equals to {farenheit} °F")
elif option == "2":
    farenheit = float(input("Insert the amount of Fahrenheit: "))
    celsius = (farenheit - 32) / 1.8
    celsius = round(celsius, 1)
    print(f"{farenheit} °F equals to {celsius} °C")
elif option == "0":
    print("Exiting...")
else:
    print("Unknown option.")
print("\nProgram ending.")