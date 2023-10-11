import matplotlib.pyplot as plt
import pandas as pd
dicSale=[{'月份':'一月','銷售數量':320},{'月份':'二月','銷售數量':480},{'月份':'三月','銷售數量':410},{'月份':'四月','銷售數量':220},{'月份':'五月','銷售數量':380},{'月份':'五月','銷售數量':520}]
p = pd.DataFrame(dicSale)
sp = (p.iloc[:,1])
print((p.iloc[1:4,0]))
print(p.iloc[:,:])
plt.plot(sp)
plt.show()