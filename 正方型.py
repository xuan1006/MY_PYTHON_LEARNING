# 請設計一個計算長方形週長和面積的函數my_ function，
# 需求是請使用者輸入兩個數字，分別放入變數x、y，
# 其中x與y分別是長方形的兩個邊，接著將x與y兩個數字透過呼叫
# my_ function傳入函數中，計算並回傳長方形的週長和面積，
# 最後將此結果印出。
def my_function(x, y):
    perimeter=(2*x)+(2*y)
    area=int((x*y)/2)
    return perimeter, area
x=int(input("plz enter x:"))
y=int(input("plz enter y:"))
perimeter, area=my_function(x, y)
print("area=", area, "perimeter=", perimeter)