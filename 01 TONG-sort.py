#桶排序
def foo(t):
    a = range(10) #新建 a 数组，范围 0~9

    for i in range(10): #初始化 a 数组
        a[i] = 0

    for j in range(len(t)): #把每个树与 a 序列匹配，并计数
        for i in range(10):
            if t[j] == i:
                a[i]+=1
    c = [] #新建 c 数组。空，用于输出
    for i in range(10): #输出，若需要从大到小输出则用 range(9,-1,-1)
        for j in range(0,a[i],1): # range(a,b,c)：从 a 起始，到 b 止，每次加 c
            c.append(i) #追加插入空数组 c
    return c #返回
