import sys
def method(string:str):
    return sum([(1 if a in ['a', 'e', 'i', 'o', 'u'] else 0) for a in string])

if len(sys.argv)>1:
    print(method(" ".join(sys.argv[1:])))
else:
    print(method(input("> ")))

