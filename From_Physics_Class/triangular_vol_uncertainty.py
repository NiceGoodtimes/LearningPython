"""VARIABLES"""
#input individual averages
mean_a = float(input("enter the average of b: ")) #takes the average of several measurements of a base
mean_b = float(input("enter the average of h: ")) #takes the average of several measurements of a height
mean_c = float(input("enter the average of t: ")) #takes the average of several measurements of a thickness

#first product in function
mean_bc = (mean_b * mean_c)/2
uncert_a = float(input("enter the uncertainty of a: ")) #takes the uncertainty of the length measurements

#second product in function
mean_ac = (mean_a * mean_c)/2
uncert_b = float(input("enter the uncertainty of b: ")) #takes the uncertainty of the width measurements

#third product in function
mean_ab = (mean_a * mean_b)/2
uncert_c = float(input("enter the uncertainty of c: ")) #takes the uncertainty of the height measurements

"""FUNCTIONS"""
#calculates the uncertainty in the volume of a rectangular prism
def calculate():
    inside = (mean_bc*uncert_a)**2 +(mean_ac*uncert_b)**2 +(mean_ab*uncert_c)**2
    uncert_volume = inside**0.5
    return uncert_volume

"""MAIN"""
print(calculate())
