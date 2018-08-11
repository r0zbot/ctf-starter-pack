line = input()
for i in range(len(line)//2):
    print('{1}{0}'.format(line[2*i], line[2*i + 1]), end='')
