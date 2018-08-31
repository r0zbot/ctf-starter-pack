line = input()
while len(line) > 0:
    char, line = line[:7], line[7:]    
    print(chr(int(char, 2)), end='')
print()

