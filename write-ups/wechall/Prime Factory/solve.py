def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sum_digits(n):
    sum = 0
    while n != 0:
        sum += n%10
        n = n//10
    return sum

def find_prime(start):
    n = start
    while not is_prime(n) or not is_prime(sum_digits(n)):
        n += 1
    return n

if __name__ == '__main__':
    start = 1000000

    first_prime  = find_prime(start)
    print('first_prime:', first_prime)

    second_prime = find_prime(first_prime + 1)
    print('second_prime:', second_prime)

    print('solution: ', first_prime, second_prime, sep='')
