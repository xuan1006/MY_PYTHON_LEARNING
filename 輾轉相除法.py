def ea(a, b):
    i=1
    if(a>=b):
        if(a%b==0):
            return (b)
        else:
            while((b*i)<a):
                i+=1
            return (ea(a-(b*(i-1)), b))
    else:
        if(b%a==0):
            return a
        else:
            while((a*i)<b):
                i+=1
            return (ea(a, b-(a*(i-1))))
# num1=int(input("plz enter num1:"))
# num2=int(input("plz enter num2:"))
num1=546
num2=429
print(ea(num1, num2))