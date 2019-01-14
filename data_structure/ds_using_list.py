shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase')

print('These items are:', end=' ')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
# shoplist.remove('rice')
# shoplist.remove(1)  wrong！！
print('I bought the', olditem)
print('My shopping list is now', shoplist)

for i in shoplist:
    print(i)
else:
    print('End')
