import re
from dna_sequencing import get_sequences


if __name__ == '__main__':
    dna = 'ACCGXXTXXYYGTTQRACQQTGGGCXTTGTXX'

    dna = re.sub(r'[^ACTGX]+', 'X', dna)

    short_sequences = get_sequences(dna)
    print(short_sequences)

