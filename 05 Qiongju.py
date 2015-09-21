#Qiongju 01
for i in range(10):
    if((i*10+3)*6528 == (30+i)*8256):
        print i
    if not i: #判断空值，Python 中没有 null 的写法
        print "The number is not found to meet the requirements."

#Qiongju 02
# XX + XX = XX

for a in range(1,5):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                for e in range(1,10):
                    for f in range(1,10):
                        if (a*10+b+c*10+d==e*10+f and
                        a!=b and a!=c and a!=d and a!=e and a!=f
                        and b!=c and b!=d and b!=e and b!=f
                        and c!=d and c!=e and c!=f
                        and d!=e and d!=f
                        and e!=f):
                            print a,b,"+",c,d,"=",e,f
                            total +=1
