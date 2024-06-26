import sys
from decimal import Decimal, getcontext

def calculate_phi(precision):
    getcontext().prec = precision + 1
   
    x = Decimal(5)
    for i in range(precision * 5):
        x = (x + Decimal(5) / x) / 2
    sqrt5 = x
    
    phi = (Decimal(1) + sqrt5) / Decimal(2)
    return phi

if __name__ == "__main__":
    if len(sys.argv) > 1:
        digits = int(sys.argv[1])  #Get number of digits from command line
    else:
        digits = 10   #Default value when there are no command line arguments

    phi = calculate_phi(digits)
    print(str(phi))
