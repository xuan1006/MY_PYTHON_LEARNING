def BMI(h,w):
    h=h/100
    bmi=w/(h*h)
    return bmi
a=int(input("輸入身高"))
b=int(input("輸入體重"))
print("BMI=%6.3f"%(BMI(a,b)))
