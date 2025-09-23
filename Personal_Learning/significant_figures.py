#notes
"""the steps refer to the image in the wikipedia article about sig figs"""

#variables
num_input = input("Enter the number: ").strip().replace(",","") #gets a number to convert
if num_input.startswith("-"):
    is_positive = False
else:
    is_positive = True

#functions
def sigfig_special(raw_sig_fig):
    p = raw_sig_fig
    if p.startswith("0.") and len(p) > 2:
        #trims insignificant zeros
        p_pre_length = len(p)
        p = p[2:]
        p = p.lstrip("0")
        p_post_length = len(p)
        zeros = p_pre_length - p_post_length - 1

        # inserting the decimal point after the first significant digit
        first_half = p[0:1]
        second_half = p[1:]
        decimal_insert = f"{first_half}.{second_half}"
        scientific_notation = f"{decimal_insert}e-{zeros}"
        return scientific_notation
    elif p.startswith("-0.") and len(p) > 3:
        #trims insignificant zeros
        p_pre_length = len(p)
        p = p[3:]
        p = p.lstrip("0")
        p_post_length = len(p)
        zeros = p_pre_length - p_post_length - 2

        # inserting the decimal point after the first significant digit
        first_half = p[0:1]
        second_half = p[1:]
        decimal_insert = f"{first_half}.{second_half}"
        scientific_notation = f"-{decimal_insert}e-{zeros}"
        return scientific_notation
    else:
        return print("error, please try again")
def sigfig_decider(x):
    if x.find("."):
        pass
    else:
        x.rstrip("0") #need to put in scientific notation
    return x

def case_1(a, action):
    #if desire is to remove the digits
    if action == "remove":
        result = sigfig_decider(a)
        return result
    elif action == "count":
        result = sigfig_decider(a)
        return len(result)
    else:
        return print("please use a number for a and either \"remove\" or \"count\". for action")


    #removes insignificant figures
def case_2(a, action):
    if action == "remove":
        return sigfig_special(a)
    elif action == "count":
        if is_positive:
            find_e = a.rfind("e")
            sigfig_digits = len(a[:find_e]) -1
            return sigfig_digits
        else:
            find_e = a.rfind("e")
            sig_fig_digits = len(a[:find_e]) -2
            return sig_fig_digits
    else:
        return print("please use a number for a and either \"remove\" or \"count\".")


#MAIN
input("Press Enter to exit.")