54

number = int(input("What number should we test? >>"))
i= 1

while i <= number:
    if (i % 3 == 0) and (i% 5 == 0):
        print("FizzBuzz") 
        
    elif (i% 3 == 0):
        print("Fizz")
        
    elif (i % 5 == 0):
        print("Buzz")
        
    else:
        print(i)
        
    i += 1