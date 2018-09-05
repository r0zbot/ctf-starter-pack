# We Chall: Prime Factory

**Categoria:** Training, Math
**Pontos:** 2
**Descrição:**

>Your task is simple:
>
>Find the first two primes above 1 million, whose separate digit sums are also prime.
>
>As example take 23, which is a prime whose digit sum, 5, is also prime.
>
>The solution is the concatination of the two numbers,
>
>Example: If the first number is 1,234,567 and the second is 8,765,432, your solution is 12345678765432
>
> Disponível em:   <https://www.wechall.net/challenge/training/prime_factory/index.php>

## Write-up
Para resolver essa challenge, o método mais fácil é criar um script em python que faça os cálculos pedidos e encontre os dois primos.

**Fonte:** [solve.py](solve.py)
```python
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

```
Com isso, encontramos a resposta.

**Resposta:** 10000331000037

## Outros Write-ups e arquivos

* Nada ainda
