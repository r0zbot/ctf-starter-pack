# We Chall: Encodings - URL encode

**Categoria:** Training, Encoding
**Pontos:** 1
**Descrição:**

> Your task is to decode the following:
>
>%59%69%70%70%65%68%21%20%59%6F%75%72%20%55%52%4C%20%69%73%20%63%68%61%6C%6C%65%6E%67%65%2F%74%72%61%69%6E%69%6E%67%2F%65%6E%63%6F%64%69%6E%67%73%2F%75%72%6C%2F%73%61%77%5F%6C%6F%74%69%6F%6E%2E%70%68%70%3F%70%3D%70%64%68%69%62%68%70%6C%6C%69%68%72%26%63%69%64%3D%35%32%23%70%61%73%73%77%6F%72%64%3D%66%69%62%72%65%5F%6F%70%74%69%63%73%20%56%65%72%79%20%77%65%6C%6C%20%64%6F%6E%65%21
>
> Disponível em:   <https://www.wechall.net/challenge/training/encodings/url/index.php>

## Write-up
Inicialmente, vemos uma sequência de números em hexadecimal separados por %. Provavelmente, cada número representa um caractere de uma frase que terá uma URL.

Por isso, podemos criar um programa curto em python para decodificar essa linha:

**Fonte:** [decode.py](decode.py)
```python
line = input().split('%')[1:]
for c in line:
    print(chr(int(c, 16)), end='')
print()
```
Assim, obtemos o texto
```
Yippeh! Your URL is challenge/training/encodings/url/saw_lotion.php?p=pdhibhpllihr&cid=52#password=fibre_optics Very well done!
```
Com a URL do WeChall, obtemos um link que, ao clicá-lo, temos a challenge completa.

**Resposta:** <https://www.wechall.net/challenge/training/encodings/url/saw_lotion.php?p=pdhibhpllihr&cid=52#password=fibre_optics>

## Outros Write-ups e arquivos

* Nada ainda
