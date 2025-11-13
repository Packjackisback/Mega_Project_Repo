import sys
if len(sys.argv)>1:
    print(" ".join(sys.argv[1:])[::-1])
else:
    print(input("Enter text to be reversed\n")[::-1])