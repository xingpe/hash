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


import hashlib, sys
m = hashlib.sha256()
hash = ""
hash_file = "hash.txt"
wordlist = "m.txt"
try:
  hashdocument = open(hash_file, "r")
except IOError:
  print("Invalid file.")
  raw_input()
  sys.exit()
else:
  hash = hashdocument.readline()
  hash = hash.replace("\n", "")

try:
  wordlistfile = open(wordlist, "r")
except IOError:
  print("Invalid file.")
  raw_input()
  sys.exit()
else:
  pass
for line in wordlistfile:
  # Flush the buffer (this caused a massive problem when placed 
  # at the beginning of the script, because the buffer kept getting
  # overwritten, thus comparing incorrect hashes)
  m = hashlib.sha256()
  line = line.replace("\n", "")
  m.update(line)
  word_hash = m.hexdigest()
  if word_hash == hash:
    print("Collision! The word corresponding to the given hash is", line)
    input()
    sys.exit()
