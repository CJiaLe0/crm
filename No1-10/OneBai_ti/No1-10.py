#实例001，数字组合
#题目：有四个数字，1、2、3、4,能组成多少个互不相同且无重复数字的三位数？各是多少？
# total=0  #组合数
# list=[]  #将组成的值给列表
# sum=0    #计数
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if (i!=j)and(i!=k)and(j!=k):
#                 total=i*100+j*10+k
#                 list.append(total)
#                 sum+=1
# print(list)
# print(sum)
# 方法二：
# import itertools
# sum2=0
# a=[1,2,3,4]
# for i in itertools.permutations(a,3):    #permutations:连续返回可迭代对象中长度为r的元素排列
#     print(i)
#     sum2+=1
# print(sum2)

# 实例2：三数排序
# raw=[]
# for i in range(3):   #输入整数%d，将循环遍历的i依次赋给%d，也就是raw
#     x=int(input('int%d:'%(i)))
#     raw.append(x)
#
# for i in range(len(raw)):
#     for j in range(i,len(raw)):
#         if raw[i]>raw[j]:
#             raw[i],raw[j]=raw[j],raw[i]
# print(raw)

# 方法二：
# raw2=[]
# for i in range(3):
#     x=int(input('int%d:'%(i)))
#     raw2.append(x)
# print(sorted(raw2))


# 实例三：copy
# import copy
# a=[1,2,3,4,[1,2,3]]
# b=a
# c=a[:]  #浅拷贝
# d=copy.copy(a)  #浅拷贝
# e=copy.deepcopy(a)  #深拷贝
#
# a.append(5)
# a[4].append('c')
#
# print('a=',a)
# print('b=',b)
# print('c=',c)
# print('d=',d)
# print('e=',e)

# 实例四：九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%2d'%(i,j,i*j),end=' ')
#     print()

# 实例五：这天第几天？
# 分析：需要分平年和闰年，闰年二月多一天。
# def isLeapYear(y):
#     return (y%400==0 or (y%4==0 and y%100!=0))
# Dofm=[0,31,28,30,31,30,31,31,30,31,30]
# res=0
# year=int(input('Year=:'))
# month=int(input('Month:'))
# day=int(input('Day:'))
# if isLeapYear(year):
#     Dofm[2]+=1
# for i in range(month):
#     res+=Dofm[i]
# print(res+day)
