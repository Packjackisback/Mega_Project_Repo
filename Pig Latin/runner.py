def word_to_pig_latin(word: str) -> str:
    # find last consonant
    last_index: int = 0
    for char in word:
        if char in ['a', 'e', 'i', 'o', 'u']:
            last_index += 1
        else:
            break;
    return word[last_index:] + word[:last_index] + "ay"

import sys
if len(sys.argv)>1:
    print(" ".join(sys.argv[1:]))
else:
    print(input("Enter text to be reversed\n")[::-1])