from dna_sequencing import get_sequences


if __name__ == '__main__':
    dna = 'ACCGXXTXXYYGTTQRACQQTGGGCXTTGTXX'
    bad_letters = []
    for cr in dna:
        if cr not in 'ACTGX' and cr not in bad_letters:
            bad_letters.append(cr)

    for cr in bad_letters:
        while cr in dna:
            dna = dna.replace(cr, 'X')

    short_sequences = get_sequences(dna)
    print(short_sequences)

