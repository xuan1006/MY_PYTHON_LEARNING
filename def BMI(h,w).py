def BMI(h, w):
    h = h / 100.0
    bmi = w / (h ** 2)
    return bmi

while True:
    w = float(input("請輸入體重kg: "))
    if w == 0:
        break
    h = float(input("請輸入身高cm: "))
    bmi = BMI(h, w)
    print(f"你的身高{h:.2f}公分, 體重 {w:.1f}公斤, bmi指數 {bmi:.2f}: ", end='')
    if bmi < 18.5:
        print('體重過輕')
    elif bmi < 24:
        print('正常範圍')
    elif bmi < 27:
        print('稍微過重')
    elif bmi < 30:
        print('輕度肥胖')
    elif bmi < 35:
        print('中度肥胖')
    else:
        print ('過度肥胖')