#SI unit lookup
#si_units = (10e12, 10e12, 10e6, 10e3, 10e2, 10e1, 10e0, 10e-1, 10e-2, 10e-3, 10e-6, 10e-9, 10e-12) #tuple
si_units = (10e0, 10e1, 10e2, 10e3, 10e4, 10e5, 10e6, 10e7, 10e8, 10e9, 10e10, 10e11, 10e12, 10e13, 10e14, 10e15,
            10e-15, 10e-14, 10e-13, 10e-12, 10e-11, 10e-10, 10e-9, 10e-8, 10e-7, 10e-6, 10e-5, 10e-4, 10e-3, 10e-2, 10e-1)
none = si_units[0] #redundancy

#functions

#allows for a v-lookup of the name of a prefix, returning num value
def si_conversion(si_input):
    power_ten = 0 #initializes the variable
#retrieves SI value
    if si_input == "tera":
        power_ten = si_units[12]
    elif si_input == "giga":
        power_ten = si_units[9]
    elif si_input == "mega":
        power_ten = si_units[6]
    elif si_input == "kilo":
        power_ten = si_units[3]
    elif si_input == "hecto":
        power_ten = si_units[2]
    elif si_input == "deca":
        power_ten = si_units[1]
    elif si_input == "base":
        power_ten = si_units[0]
    elif si_input == "deci":
        power_ten = si_units[-1]
    elif si_input == "centi":
        power_ten = si_units[-2]
    elif si_input == "milli":
        power_ten = si_units[-3]
    elif si_input == "micro":
        power_ten = si_units[-6]
    elif si_input == "nano":
        power_ten = si_units[-9]
    elif si_input == "pico":
        power_ten = si_units[-12]
    else:
        print("SI prefix error, please try again without a '-'")
        input("Press enter to exit...")
        exit()

    return power_ten

#takes the magnitude of the input as a float
def significand():
    #will keep asking for a number until only a number is given
    while True:
        try:
            sig = float(input("Enter the number to be converted: ").strip())
            break
        except ValueError:
            print("Please enter a number.")
    return sig

#returns the si prefix as a number
def enter_si_prefix():
    si_prefix = input("Enter SI Prefix: ").strip().lower() #gets the desired input
    result = si_conversion(si_prefix)
    return result

#returns the desired si output as a number
def enter_si_output():
    si_output = input("What SI prefix convert to: ")
    result = si_conversion(si_output)
    return result

#heart of the conversion
def conversion():
    true_value_input = significand() * enter_si_prefix()
    pre_result = true_value_input / enter_si_output()
    result = f"{pre_result:.3E}"
    return result

print(conversion())
input("Press enter to exit...")