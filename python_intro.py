print('Hello World')
name = 'Marie'
name = 'Ole'
print(name)

if name == 'Marie':
    print ('It works!')
elif name == 'Ole':
    print ('Hey ' + name)
else:
    print ('Why you so stupid?')

def coolness():
    print('Heeeyy!')
    print('How you doing?')

coolness()
def coolness(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

coolness('Ola')

def hi(name):
    print('Hello ' + name + '!')

girls = ['Guro', 'Tora', 'Astri', 'Sunniva']
for name in girls:
    hi(name)
    print('Next girl')

for i in range(0,10):
    print (i)
