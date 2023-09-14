#請使用者輸入一個數字，放入變數num。
# 接著開始使用wh ile迴圈建構主要邏輯：如果num不等於3的倍數，
# 則輸出字串「3N」；但如果使用者輸入了3的倍數，則輸出字串「3Y」
# ；如果使用者輸入了999，則迴圈完成，印出「結束」。
num=0
while(num!=999):
    num=int(input("plz enter num:"))
    if(num%3==0):
        print("3Y")
    else:
        print("3N")
print("end!")