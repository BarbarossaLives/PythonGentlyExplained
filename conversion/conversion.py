def convert_f(degree_c):
    F=(degree_c*(9/5)) +32
    return F

def convert_c(degree_f):
    C=((degree_f-32)*(5/9))
    return C


print("What tempature woould you like to convert?  ")
temp = int(input(">>"))  
print("(F)erenheit to Celcius or (C)elcuis to Ferenheit? ")
convert = input("F or C .>>")
if convert == "C" or "c":
    answer = convert_c(temp)
    print(str(answer))

else:
    answer = convert_f(temp)
    print(str(answer))
    
    
