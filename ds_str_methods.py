name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes, the String startwiih "Swa"')

if 'a' in name:
    print('Yes ,it contains the char "a"')

if name.find('war') != -1:
    print('Yes, it contains the string "war"')

delimiter = '_*_'
mylist = ['brazil', 'Russia', 'India']
print(delimiter.join(mylist))
