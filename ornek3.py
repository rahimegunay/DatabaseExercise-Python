def dna_to_rna(dna):
    new = ""

    for i in dna:
        if i == 'A':
            new += 'A'
        elif i == 'C':
            new += 'C'
        elif i == 'T':
            new += 'U'
        else:
            new += 'G'
    return(new)