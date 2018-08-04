line = input().split('%')[1:]
for c in line:
    print(chr(int(c, 16)), end='')
print()
	
