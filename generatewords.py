import random

alphabet=input('hash: ')
s=''
file=open('m.txt','a')
for count in range(0, 100000):
  for x in random.sample(alphabet, 64):
    s+=x
  file.write(s+'\n')
  s=''
file.close()
print('DONE')
