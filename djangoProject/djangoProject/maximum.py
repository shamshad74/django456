from functools import reduce
#
# lst=[2,6,7,8]
#
# mx=reduce(lambda n1,n2:n1 if n1>n2 else n2,lst)
#
# mn=reduce(lambda n1,n2:n1 if n1<n2 else n2)
# product=reduce(lambda n1,n2:n1*n2,lst)
# print(mx)
# print(mn)
# print(product)

lst=["2","6","7","8"]
lst.sort(reverse=True)
print(lst)
# acc=reduce(lambda n1,n2:n1+n2,lst)
# print(acc)
acc=reduce(lambda n1,n2:(n1+n2) if int(n1+n2)>int(n2+n1) else (n2+n1),lst)
print(acc)