# Complete the function that takes a string of English-language text and returns the number of consonants in the string.
# Consonants are all letters used to write English excluding the vowels a, e, i, o, u.

# Examples
@test.it("works for some examples")
#    def sample_tests():
#        test.assert_equals(consonant_count(''), 0, 'Test string is empty string');
#        test.assert_equals(consonant_count('aaaaa'), 0, 'Test string: "aaaaa"');
#        test.assert_equals(consonant_count('XaeiouX'), 2, 'Test string: "XaeiouX"');
#        test.assert_equals(consonant_count('Bbbbb'), 5, 'Test string: "Bbbbb"');
#        test.assert_equals(consonant_count('helLo world'), 7, 'Test string: "helLo world"');
#        test.assert_equals(consonant_count('h^$&^#$&^elLo world'), 7, 'Test string: "h^$&^#$&^elLo world"');

def consonant_count(s):
    print(s)
    count = 0
    for i in s:
        if i.lower() in 'bcdfghjklmnpqrstvwxyz':
            count += 1
    print(count)
    return count
