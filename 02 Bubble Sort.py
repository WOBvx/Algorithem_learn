#冒泡排序
def bubble(a):
    x = list(a) # 可以将元组Tuple eg.(1,2,4,1) 转换成列表list [1,2,4,1]
    n = len(x)
    for i in range(1,n,1):
        for j in range(0,n-i,1):
                if(x[j]<x[j+1]):
                    t = x[j]
                    x[j] = x[j+1]
                    x[j+1] = t
    return x
