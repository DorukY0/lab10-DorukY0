
def factorial(n):
    i=1
    result=1
    if  n==0:
        result=1
    else:
        while i<n:
            result=result*(i+1)
            i=i+1
    
    return result
if factorial(3)==6:
    print("no errors.")
    
