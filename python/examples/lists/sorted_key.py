animals = ['chicken', 'cow', 'snail', 'elephant']
print(sorted(animals))          # ['chicken', 'cow', 'elephant', 'snail']
srt = sorted(animals, key=len)
print(srt)                      # ['cow', 'snail', 'chicken', 'elephant']
