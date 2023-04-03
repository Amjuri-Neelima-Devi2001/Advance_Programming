# l=[1,2,3]
# l.append('ab')
# l.extend('400')
# # print(l)
# d={[10]:(1,2,3)}
# print(d.values())
# def demo_call_by_ref(l):
#     l.append(20)
#     print(l)
# l=[1,2,34]
# print("before call by ref is {}".format(l))
# print("After call by ref is")
# demo_call_by_ref(l)
# def demo_call_by_value(a,b):
#     print(a,b)
#     a=100
#     b=200
# a=10
# b=20
# demo_call_by_value(a,b)
# print(a,b)
# l=([1,2,3],[15,67])
# l[0][1]=45
# print(l)

# class outerclass:
#     def __init__(self):
#         self.x=10
#     class innerclass:
#         def __init__(self):
#             self.y=100
#         def inner_method(self):
#             print("Inner Method")
# outer=outerclass()
# inner=outer.innerclass()
# print(inner.y)

import re
l="hello, neel bza12378 you bza132 are in bza1234"
rl=re.findall(r'bza[1-5]{3}',l)
print(rl)
count=0
for i in rl:
    count+=1
print(count)
