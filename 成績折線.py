import pandas as pd
import os
import matplotlib.pyplot as plt
rc= [{'姓名':'','python':0,'資工導論':0}]
fp = "csie2AB.json"
if os.path.isfile(fp):
    pf=pd.read_json(fp)
else:
    pf=pd.DataFrame(rc)
    pf=pf.drop(0)
name=''
while(1):
    na=input('輸入姓名:')
    if(na==''):
        break
    py=int(input('輸入python成績'))
    cs=int(input('輸入資工導論成績:'))
    le1=len(pf)
    pf.loc[le1,'姓名']=na
    pf.loc[le1,'python']=py
    pf.loc[le1,'資工導論']=cs
sa=(pf.iloc[:,1])
x = len(pf.iloc[:,1])
plt.plot(sa)
plt.show()
pf.to_json(fp)
print(pf.iloc[:,:])