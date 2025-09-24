"""VARIABLES"""
#widths
w1 = float(input("Average Width 1: "))
w2 = float(input("Average Width 2: "))
w3 = float(input("Average Width 3: "))
#lengths
l1 = float(input("Average Length 1: "))
l2 = float(input("Average Length 2: "))
l3 = float(input("Average Length 3: "))
#thickness
t0 = float(input("Average Thickness: "))

"""CALCULATED PARTIAL DERIVATIVES"""
#first term
mean_t0w3 = w3 * t0
uncert_l3 = float(input("Uncertainty of Width 3: "))
#second term
mean_t0l3 = t0 * l3
uncert_w3 = float(input("Uncertainty of Length 3: "))
#third term
mean_t0w2 = t0 * w2
uncert_l1 = float(input("Uncertainty of Length 1: "))
#fourth term
mean_t0l1 = t0 * l1
uncert_w2 = float(input("Uncertainty of Width 2: "))
#fifth term
mean_l3w3 = l3 * w3
uncert_t0 = float(input("Uncertainty of Thickness: "))

"""FUNCTIONS"""
def calculate():
    term1 = (mean_t0w3 * uncert_l3) ** 2
    term2 = (mean_t0l3 * uncert_w3) ** 2
    term3 = (mean_t0w2 * uncert_l1) ** 2
    term4 = (mean_t0l1 * uncert_w2) ** 2
    term5 = (mean_l3w3 * uncert_t0) ** 2

    inside_bit = term1 + term2 + term3 + term4 + term5
    uncert_volume = inside_bit ** 0.5
    return uncert_volume

"""MAIN"""
print(calculate())