s=[]
a='M'
b=''
while(a!=''):
    a=input('輸入A(新增) R(刪除) L(顯示),按Enter結束')
    if(a==''):
        break
    if(a=="A" or a=="a"):
        print("輸入新增名",end=":")
        b=input()
        if(b!=''):
            s.append(b)
    if(a=="R" or a=="r"):
        print("刪除名",end=":")
        b=input()
        s.remove(b)
    if(a=="L" or a=="l"):
        for i in range(len(s)):
            print("%d\t%s"%(i+1,s[i]))
