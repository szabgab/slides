from dna_sequencing import get_sequences


if __name__ == '__main__':
    dna = 'ACCGXXTXXYYGTTQRACQQTGGGCXTTGTXX'

    filtered = []
    for cr in dna:
        if cr in 'ACGT':
            filtered.append(cr)
        else:
            filtered.append('X')
    #print(filtered)

    dna = ''.join(filtered)

    short_sequences = get_sequences(dna)
    print(short_sequences)

