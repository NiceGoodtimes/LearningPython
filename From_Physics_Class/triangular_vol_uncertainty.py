"""VARIABLES"""
#input individual averages
mean_base = float(input("enter the average of the base: ")) #takes the average of several measurements of a base
mean_height = float(input("enter the average of the height: ")) #takes the average of several measurements of a height
mean_thickness = float(input("enter the average of the thickness: ")) #takes the average of several measurements of a thickness

#first product in function
mean_bc = (mean_height * mean_thickness)/2
uncert_base = float(input("enter the uncertainty of the base: ")) #takes the uncertainty of the length measurements

#second product in function
mean_ac = (mean_base * mean_thickness)/2
uncert_height = float(input("enter the uncertainty of the height: ")) #takes the uncertainty of the width measurements

#third product in function
mean_ab = (mean_base * mean_thickness)/2
uncert_thickness = float(input("enter the uncertainty of the thickness: ")) #takes the uncertainty of the height measurements

"""FUNCTIONS"""
#calculates the uncertainty in the volume of a rectangular prism
def calculate():
    inside = (mean_bc*uncert_base)**2 +(mean_ac*uncert_height)**2 +(mean_ab*uncert_thickness)**2
    uncert_volume = inside**0.5
    return uncert_volume

"""MAIN"""
print(calculate())
