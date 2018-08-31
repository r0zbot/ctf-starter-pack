# We Chall: Training: ASCII

**Categoria:** Training, Encoding
**Pontos:** 1
**Descrição:**

>In a computer, you can only work with numbers.
>
>In this challenge you have to decode the following message, which is in ASCII.
>
> 84, 104, 101, 32, 115, 111, 108, 117, 116, 105, 111, 110, 32, 105, 115, 58, 32, 110, 99, 112, 114, 115, 105, 111, 103, 110, 100, 98, 99
>
> Disponível em: <https://www.wechall.net/challenge/training/encodings/ascii/index.php>

## Write-up
Pelo enunciado da challenge, sabemos que os números representam caracteres ASCII. Por isso, podemos criar um programa curto em python para transformar esses números em caracteres:

**Fonte:** [decode.py](decode.py)
```python
line = input().split(', ')
for char in line:
    print(chr(int(char)), end='')
print()
```
Assim, obtemos o texto
```
The solution is: ncprsiogndbc
```

**Resposta:** ncprsiogndbc
## Outros Write-ups e arquivos

* Nada ainda
