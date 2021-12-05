import random
vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

def random_name():
    word = ""
    word_length = random.randrange(2,6)
    for i in range(word_length):
        # more consonants than vowels
        if random.randrange(0,3) == 0:
            # add couplets, creates more "natural" names
            word += random.choice(vowels)
            word += random.choice(consonants)
        else:
            word += random.choice(consonants)
            word += random.choice(vowels)

    # add another letter sometimes so name isn't always of even length
    if random.randrange(0,1) == 0:
        # sometimes consonant
        if random.randrange(0,1) == 0:
            word += random.choice(consonants)
        # sometimes vowel
        else:
            word += random.choice(vowels)

    return word