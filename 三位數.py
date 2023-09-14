# 請使用0/2/4/6/8五個數字產出三位不同數字的三位數，
# 並計算這樣的數字有少個。舉例來說，246就是一個這樣的三位數，
# 個位、十位、百位數字均不同；866就不是這樣的數字，因為個位、
# 十位數字相同；同時要注意048這樣的數字也不合規定，
# 因為這並不是一個三位數。
for hh in range(2, 8+1, 2):
    for tt in range(0, 8+1, 2):
        for oo in range(0, 8+1, 2):
            if(not(hh==tt or tt==oo or hh==oo) and not(hh==tt and tt==oo and hh==oo)):
                print((100*hh)+(10*tt)+oo)