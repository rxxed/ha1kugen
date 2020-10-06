import random
from nltk.corpus import words

complexity = 'en-basic'

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


def addrandomcomma(first, second, third):
    to_add = random.randint(0, 1)
    if to_add == 0:
        return first, second, third
    who_to_add = random.randint(1, 3)
    if who_to_add == 1:
        size = len(first)
        i = random.randint(0, size-1)
        first[i] = first[i] + ','
    if who_to_add == 2:
        size = len(second)
        i = random.randint(0, size-1)
        second[i] = second[i] + ','
    if who_to_add == 3:
        size = len(third)
        i = random.randint(0, size-1)
        third[i] = third[i] + ','

    return first, second, third


def genhaiku():
    first = getnsyllwords(5)
    second = getnsyllwords(7)
    third = getnsyllwords(5)

    first, second, third = addrandomcomma(first, second, third)

    return ' '.join(first), ' '.join(second), ' '.join(third)
