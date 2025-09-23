#input individual averages
mean_a = float(input("enter the average of a: "))
mean_b = float(input("enter the average of b: "))
mean_c = float(input("enter the average of c: "))

mean_bc = mean_b * mean_c
uncert_a = float(input("enter the uncertainty of a: "))

mean_ac = mean_a * mean_c
uncert_b = float(input("enter the uncertainty of b: "))

mean_ab = mean_a * mean_b
uncert_c = float(input("enter the uncertainty of c: "))

def calculate():
    inside = (mean_bc*uncert_a)**2 +(mean_ac*uncert_b)**2 +(mean_ab*uncert_c)**2
    uncert_volume = inside**0.5
    return uncert_volume

print(calculate())