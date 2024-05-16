import sys
from decimal import Decimal, getcontext

def sqrt_2(precision):
    getcontext().prec = precision + 1
    x = Decimal(2)  
    for i in range(precision * 5):
        x = (x + Decimal(2) / x) / 2
    return x

if __name__ == "__main__":
    if len(sys.argv) > 1:
        digits = int(sys.argv[1])  #Get number of digits from command line
    else:
        digits = 10  #Default value when there are no command line arguments

    root2 = sqrt_2(digits)
    print(str(root2))
