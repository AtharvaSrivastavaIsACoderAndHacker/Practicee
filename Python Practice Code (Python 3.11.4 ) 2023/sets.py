s = {'hello', '29',9,True,'hola'}
print(s)

print('----------------------------------------------------------------------------------------')
ss = set()
ss - {1,2,3,4,5,9}
print(ss)
print('----------------------------------------------------------------------------------------')
for i in s:
    print('*',i)

print('----------------------------------------------------------------------------------------')
union = s.union(ss)
print(union)
s.update(ss)

print('----------------------------------------------------------------------------------------')


intUPDATE = s.intersection_update(ss)
print(intUPDATE)
print("hola")

print('----------------------------------------------------------------------------------------')
sym = s.symmetric_difference(ss)
print(sym) 

print('----------------------------------------------------------------------------------------')

diff = s.difference(ss)
print(diff) 
  
print('----------------------------------------------------------------------------------------')

isdis = s.isdisjoint(ss)
print(isdis) 

print('----------------------------------------------------------------------------------------')
superset = s.issuperset(ss)
print(superset)
print('----------------------------------------------------------------------------------------') 
s.discard('hola')
print(s)
print('----------------------------------------------------------------------------------------') 
# ssss = {'loading.','hello'}
# em = ss.pop()
# print(ss)
print('----------------------------------------------------------------------------------------')
s.clear()




del ss