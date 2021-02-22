import string
import random
from random import sample
 
 
 
#============ Word List Gen ============
minimum=int(input('Please enter the minimum length of any give word to be generated: '))
maximum=int(input('Please enter the maximum length of any give word to be generated: '))
wmaximum=int(input('Please enter the max number of words to be generate in the dictionary: '))
 
alphabet = '680113444f795fd49455201055ad275cb5feeed63e90be77e3fe7019909522c3'
string=''
xrange=range
file = open("m.txt","a")
for count in xrange(0,wmaximum):
  for x in random.sample(alphabet,random.randint(minimum,maximum)):
      string+=x
  file.write(string+'\n')
  string=''
file.close()
print ('DONE!')
 
#============    WLG END    ============
#Begin Hash Cracker.py
 
import hashlib, sys
m = hashlib.sha256()
hash = ""
hash_file = 'hash.txt'
wordlist = 'm.txt'
try:
        hashdocument = open(hash_file,"r")
except IOError:
        print ("Invalid file.")
        input()
        sys.exit()
else:
        hash = hashdocument.readline()
        hash = hash.replace("\n","")
        
try:
        wordlistfile = open(wordlist,"r")
except IOError:
        print ("Invalid file.")
        input()
        sys.exit()
else:
        pass
for line in wordlistfile:
        m = hashlib.sha256()  #flush the buffer (this caused a massive problem when placed at the beginning of the script, because the buffer kept getting overwritten, thus comparing incorrect hashes)
        line = line.replace("\n","")
        m.update(line.encode(wordlistfile.encoding))
        word_hash = m.hexdigest()
        if word_hash==hash:
               print ("Collision!  The word corresponding to the given hash is", line,)
               input()
               sys.exit()
 
print ("The hash given does not correspond to any supplied word in the wordlist.")
input()
sys.exit()
