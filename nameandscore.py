name=[]
score=[]
a=''
while(1):
    a=input("輸入選項A(新增)R(刪除)L(顯示)，案Enter結束")
    if a=='':
        break
    if(a=='A' or a=='a'):
        na=input("輸入新增名")
        num=input("輸入成績")
        name.append(na)
        score.append(num)
    elif(a=='R' or a=='r'):
        na=input("輸入刪除名")
        if na in name:
            index=name.index(na)
            name.pop(index)
            score.pop(index)
    elif(a=='L' or a=='l'):
        for i in range(0,len(name)):
            print(i+1,'\t',name[i],'\t',score[i],'\n')
    a=''