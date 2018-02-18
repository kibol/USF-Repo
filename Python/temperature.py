def get_input():
    x = input("Enter the temperature in Celsius below \n")  
    return x
   
    
def calc_temp (cel):
    y = (cel*9/5.0 + 32)
    return y  
    

cent = get_input()
fahr = calc_temp(cent)

print " Your entry of", cent , "Celcius is ", fahr ,"Fahrenheit",



