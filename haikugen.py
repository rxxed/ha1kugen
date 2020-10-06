import random
from nltk.corpus import words

complexity = 'en'


def syllcount(the_text):

    clean_text = ""
    for ch in the_text:
        if ch in "abcdefghijklmnopqrstuvwxyz'’":
            clean_text += ch
        else:
            clean_text += " "

    as_vow    = "aeiouy'’"
    d_exep    = ("ei","ie","ua","ia","eo")
    the_words = clean_text.lower().split()
    all_sylls = 0
    for in_word in the_words:
        nchar  = len(in_word)
        nsyll  = 0
        was_vow = False
        was_y   = False
        if nchar == 0:
            continue
        if in_word[0] in as_vow:
            nsyll += 1
            was_vow = True
            was_y   = in_word[0] == "y"
        for c in range(1,nchar):
            is_vow  = False
            if in_word[c] in as_vow:
                nsyll += 1
                is_vow = True
            if is_vow and was_vow:
                nsyll -= 1
            if is_vow and was_y:
                nsyll -= 1
            if in_word[c:c+2] in d_exep:
                nsyll += 1
            was_vow = is_vow
            was_y   = in_word[c] == "y"
        if in_word.endswith(("e")):
            nsyll -= 1
        if in_word.endswith(("le","ea","io")):
            nsyll += 1
        if nsyll < 1:
            nsyll = 1
        # print("%-15s: %d" % (in_word,nsyll))
        all_sylls += nsyll

    if len(the_words) == 0:
        return 0
    return int(all_sylls/len(the_words))


def getnsyllwords(n):
    nsyll = 0
    ret = []
    for i in range(100):
        word = random.choice(words.words(complexity))
        if syllcount(word) == 0:
            continue
        nsyll = nsyll + syllcount(word)
        if nsyll > n:
            continue
        elif nsyll == n:
            ret.append(word)
            return ret
        ret.append(word)
    return ret

first = ' '.join(getnsyllwords(5))
second = ' '.join(getnsyllwords(7))
third = ' '.join(getnsyllwords(5))

print(first)
print(second)
print(third)
