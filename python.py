# from collections import Counter
# # Counter() Method:it is like a dictionary it returns the [descending sorted dictionary] based on values
# # Sample dictionary
# sample_dict = {1: 5, 3: 2, 2: 8, 0: 1}

# # Sorting using a for loop
# s=Counter(sample_dict)

# print(s)

# # output:Counter({2: 8, 1: 5, 3: 2, 0: 1})

# print(s[2]) #----> output 5

# l1=[2,4,1,3]
# l2=[7,5,6,8]
# l=[]
# for i in zip(l1,l2):
#     l.append(list(i))
#     print(i)
# print(l)
# l.sort(key=lambda x:x[1])
# print(l)

# ans=lambda x:x*x
# l=[1,2,3,4,5]
# print(ans(l[4]))

# n=5
# l=[]
# for i in range(n):
#     l.append('.'*n)
# # print(l)
# l[0]=l[0][:3]+'Q'+l[0][4:n]
# print(l)
# if str(5)=='5':
#     print("yes")
# else:
#     print("no")

# s=""
# for i in range(1,4):
#     s=s+str(i)
# print(s)
# l=['1','2','3']
# print("".join(l))
# print(-3%10)
# l=[0]*5
# print(l)
# Python implementation of above approach

# import math
# print(math.ceil(15/4))

# d={'a':4,'b':2}
# k=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
# print(k)

# l=[1,1,1,0]
# print(l.count(1),l.count(0))
# import copy
# l=[[1,2,3],[4,5,6]]
# ans=copy.deepcopy(l)
# ans[0][0]=5
# print(ans)
# print(l)
d1={'a':1,'b':1,'c':1}
d2={'c':1,'b':1,'a':1}
if d1==d2:
    print(d1.items())




    





