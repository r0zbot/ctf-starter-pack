# We Chall: Training: Encodings I

**Categoria:** Training, Encoding
**Pontos:** 2
**Descrição:**

> We intercepted this message from one challenger to another, maybe you can find out what they were talking about.
>
> To help you on your progress I coded a small java application, called JPK.
>
> Note: The message is most likely in english.
>
> Disponível em:   <https://www.wechall.net/challenge/training/encodings1/index.php>

## Write-up
Inicialmente, vemos uma sequência em binário. Pelo enunciado, sabemos que o texto estará em inglês. Assim, uma possibilidade é que esteja codificado em ASCII.

Porém, texto total tem 455 bits, ou seja, seus fatores são 1, 5, 7, 13, 35, 65, 91 e 455. Logo, o ASCII de 8 bits não é uma opção.

Mas ainda existe o ASCII de 7 bits (porque existe um bit excedente no formato padrão). Assim, se não quisermos usar o programa do enunciado, podemos criar um pequeno script em python que decodifica essa mensagem.

**Fonte:** [decode.py](decode.py)
```python
line = input()
while len(line) > 0:
    char, line = line[:7], line[7:]    
    print(chr(int(char, 2)), end='')
print()
```
Assim, obtemos o texto
```
This text is 7-bit encoded ascii. Your password is easystarter.
```
**Resposta:** easystarter

## Outros Write-ups e arquivos

* Nada ainda
