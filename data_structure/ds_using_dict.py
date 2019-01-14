ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print('Swaroop\'s address us', ab['Swaroop'])

del ab['Spammer']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print('\nGuido\'s address is', ab['Guido'])

for a in ab:
    print("key = {}, value = {}".format(a, ab[a]), end='\n')

if 'F' in '1f3':
    print('YES!!!')

print('f'.index('f'))
