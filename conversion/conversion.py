def convert_f(degree_c):
    F=(degree_c*(9/5)) +32
    return F

def convert_c(degree_f):
    C=((degree_f-32)*(5/9))
    return C






assert convert_c(180) == 82.22222222222223
assert convert_c(convert_f(15)) == 15
assert convert_f(0) == 32
assert convert_f(100) == 212
assert convert_c(0) == -17.77777777777778
