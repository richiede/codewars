def DNA_strand(dna):
    """
    Takes a string of characters A, T, G, C, Translates and outputs to a
    string of the complementary DNA. Reverses A to T's and G to C's (and vise versa)
    Example
    'ATTGC' --> 'TAACG'
    'GTAT' --> 'CATA'
    """
    trans_dna = ''  # creates an empty target string
    if len(dna) == 0:
        return trans_dna # if dna is empty, returns an empty string
    else:
        # for loop to reverse A - T and G - C
        for i in range(len(dna)):
            if dna[i] == 'A':
                trans_dna += 'T'
            elif dna[i] == 'T':
                trans_dna += 'A'
            elif dna[i] == 'G':
                trans_dna += 'C'
            elif dna[i] == 'C':
                trans_dna += 'G'
            else:
                # if NA character entered, message printed to screen of error
                print('Something went wrong')
                break
    return(trans_dna)

dna = ['A','A','A','A']
print(DNA_strand(dna))

# shouldBe` [T,A,C,G]
