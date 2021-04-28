import matplotlib.pyplot as xx

Lenguages = ['py', 'java', 'c++', 'ts','php']
Poll = [50,10,20,10, 10]

xx.bar(Lenguages, Poll)
xx.title ('Most used lenguages')
xx.xlabel('types of lenguage')
xx.ylabel('percentage use')

xx.savefig('GraphicExample.png')
xx.show()