import sys
from decimal import Decimal, getcontext

def sqrt_5(precision):
    getcontext().prec = precision + 1
    x = Decimal(5)  
    for i in range(precision * 5):  
        x = (x + Decimal(5) / x) / 2
    return x

if __name__ == "__main__":
    if len(sys.argv) > 1:
        digits = int(sys.argv[1])  #Get number of digits from command line
    else:
        digits = 10  #Default value when there are no command line arguments

    root5 = sqrt_5(digits)
    print(str(root5))
