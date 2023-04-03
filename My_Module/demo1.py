from collections import defaultdict
dd=defaultdict(float)
ds=defaultdict(int)
incomes=[('books',1250.00),('books',1300.00),('books',1420.00),('course',3400.00),('course',1234.00),('marks',234.00),('marks',231.00)]
for d,e in incomes:
    dd[d]=dd[d]+e
print(dd)