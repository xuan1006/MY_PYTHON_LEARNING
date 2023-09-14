import numpy as np
d=0
while(1):
    d=float(input('輸入角度:'))
    if(d==-999):
        break
    d2r=np.deg2rad(d)
    s=np.sin(d2r)
    t=np.tan(d2r)
    print('sin(%d)=%4.2f'%(d,s))
    print('tan(%d)=%4.2f'%(d,t))
