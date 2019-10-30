files = glob.glob("*.dna")
count = len(files)
batch = count/n

#files[0 : batch]
#files[batch : 2 * batch]
#...
#files[(n-1) * batch : n * batch]

for i in range(0, n):
   pid = fork()
   if pid:
       # parent
   else:
       # child
       child(files[i * batch : (i+1) * batch])

