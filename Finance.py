import math
def cost():
    r = float(input("Enter a radius in meters: "))
    p = float(input("Enter the price of the material per square meter: "))
    cost = (4 * math.pi * r**2) * p
    print(cost)
    
def sum(N):
    sum = N
    for i in range(N) :
        if i == 2 or i == 3 :
            sum += i
    return(sum)

def growthRate():
    Pp = float(input("Enter the present population: "))
    R = float(input("Enter the rate of growth: "))
    n = int(input("Enter the number of periods: "))
    Pr = Pp * (1 + R)** n
    return(Pr)
    
def simpleInterest():
    Pr = float(input("Enter the principal: "))
    R = float(input("Enter the annual rate: "))
    R = Rate /  100
    T = float(input("Enter the period: "))
    Future_Value = Pr * (1 + (R * T))
    return(Future_Value)

def compoundInterest():
    Pr = float(input("Enter the principal: "))
    R = float(input("Enter the annual rate: "))
    R =Rate / 100
    T = float(input("Enter the period(years): "))
    compounding_per_year = int(input("Enter the amount of compounding per year: "))
    Future_Value = Pr * (1 + (R / compounding_per_year)) ** (T * compounding_per_year)
    return(Future_Value)

def GDC(num_1,num_2):
    if (num_1 < num_2):
        while (num_1 > 0):
            i = num_2 % num_1
            num_2,num_1 = num_1,i
            return (i)
    else :
        while (num_2 > 0):
            i = num_1 % num_1
            num_1,num_2 = num_2,i
            return(i)
        
        
            
        
        
  
    



    
    
    
    
