# Without ufunc, we can use Python's built-in zip() method:
a=[1,2,3,4,5]
b=[6,7,8,9,10]
c=[]
for i,j in zip(a,b):
    c.append(i+j)
    print(c)