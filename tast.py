import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
plt.rcParams["font.family"]="Microsoft YaHei"
data = {
    '姓名': ['林可', '林襄', '凱蒂', '妮可', '曼容'],
    'Python': [80, 75, 93, 86, 90],
    '3D模型': [63, 56, 90, 85, 70],
    'Linux': [90, 56, 88, 68, 40],
    '資工導論': [60, 50, 40, 50, 60]
}

df = pd.DataFrame(data)
print(df)
df.plot(x="姓名",y="資工導論",kind="bar")

plt.show()

