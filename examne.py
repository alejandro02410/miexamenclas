import random
import string
archivo = open('miexamen/bdtb.txt','w')

c1 = []
c2 = []
c3 = []
c4 = []

for i in range(500):

    c1.append(random.randint(0,5000))

    c2.append(random.choice(string.ascii_letters))

    c3.append(random.randint(0,5000))

    c4.append(random.randint(0,5000))

for j in range(500):
    archivo.write('{}, {}, {}, {}\n'.format(c1[j],c2[j],c3[j], c4[j]))
archivo.close()