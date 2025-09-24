#variables
inputChoice = input("Convert from: ").strip().upper()
outputChoice = input("Convert to: ").strip().upper()

#functions
def f_to_c(x):
    a = x - 32
    return a * (5/9)
def c_to_f(x):
    a = x * (9/5)
    return a + 32
def enter_degrees():
    x = float(input("enter temperature in degrees: "))
    return x


#fahrenheit input
if inputChoice == "F":
    if outputChoice == "C":
        print(f_to_c(enter_degrees()))
    elif outputChoice == "K":
        print(f_to_c(enter_degrees()) + 273)
    elif outputChoice == "F":
        print("No need to convert.\n", enter_degrees())
    else:
        print("Uh Oh. Something went wrong.\nmake sure you entered either C, F, or K.")

#celsius input
elif inputChoice == "C":
    if outputChoice == "F":
        print(c_to_f(enter_degrees()))
    elif outputChoice == "K":
        print(enter_degrees() + 273)
    elif outputChoice == "C":
        print("No need to convert.\n", enter_degrees())
    else:
        print("Uh Oh. Something went wrong.\nmake sure you entered either C, F, or K.")

#kelvin input
elif inputChoice == "K":
    Kelvin = enter_degrees()
    #kelvin domain check
    if enter_degrees() < 0:
        print("Kelvin cannot be negative")
        exit()
#true conversion
    if outputChoice == "F":
        print(c_to_f(enter_degrees()-273))
    elif outputChoice == "C":
        print(enter_degrees() - 273)
    elif outputChoice == "K":
        print("No need to convert.\n", enter_degrees())
    else:
        print("Uh Oh. Something went wrong.\nmake sure you entered either C, F, or K.")
else:
    print("please enter either C, F, or K.")
#prevents auto-closing
input("Press enter to exit...")