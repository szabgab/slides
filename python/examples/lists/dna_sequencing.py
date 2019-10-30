dna = 'ACCGXXCXXGTTACTGGGCXTTGT'
sequences = dna.split('X')
sequences.sort(key=len, reverse=True)

new_seq = []
for w in sequences:
   if len(w) > 0:
      new_seq.append(w)

print(sequences)
print(new_seq)
