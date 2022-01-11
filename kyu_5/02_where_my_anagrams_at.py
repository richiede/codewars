def anagrams(word, words):
    """
     A function that will find all the anagrams of a word from a list,
     given two inputs: a word and an array with words.
     EXAMPLE: anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
    """
    word_sorted = [x for x in word]
    word_sorted.sort()
    correct_words = []
    for i in words:
        indi = [x for x in i]
        indi.sort()
        if indi == word_sorted:
            correct_words.append(i)
    return(correct_words)

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
