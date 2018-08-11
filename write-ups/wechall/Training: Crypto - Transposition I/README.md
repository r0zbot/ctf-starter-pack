# We Chall: Training: Crypto - Transposition I

**Categoria:** Training, Crypto
**Pontos:** 1
**Descrição:**

> It seems that the simple substitution ciphers are too easy for you.
>
>From my own experience I can tell that transposition ciphers are more difficult to attack.
>
> However, in this training challenge you should have not much problems to reveal the plaintext.
>
> `oWdnreuf.lY uoc nar ae dht eemssga eaw yebttrew eh nht eelttre sra enic roertco drre . Ihtni koy uowlu dilekt  oes eoyrup sawsro don:wg iriahpceln.g`
>
> Disponível em: https://www.wechall.net/challenge/training/crypto/transposition1/index.php

## Write-up
Inicialmente, pelo enunciado vemos que a frase de interesse está codificada pela [Cifra de transposição](https://en.wikipedia.org/wiki/Transposition_cipher).

Analisando com atenção, podemos inferir que a primeira palavra pode ser `Wonderful`. Assim, podemos usar isso para descobrir que tipo de transposição foi usada na frase.

Comparando as duas primeiras palavras
```
Wonderful
oWdnreuf.lY
```
Conseguimos observar um padrão que a transposição foi permutar dois caracteres consecutivos da forma:

```
W o n d e r f u l .  =>  o W d n r e u f .  l
1 2 3 4 5 6 7 8 9 10     2 1 4 3 6 5 8 7 10 9
```
Assim, podemos criar um pequeno script em python para decodificar a frase inteira:

**Fonte:** [decode_transposition.py](decode_transposition.py)
```python
line = input()
for i in range(len(line)//2):
    print('{1}{0}'.format(line[2*i], line[2*i + 1]), end='')
```
Encontrando a frase `Wonderful. You can read the message way better when the letters are in correct order. I think you would like to see your password now: griaiphecnlg.`.

Dessa forma, encontramos a resposta.

**Resposta:** `griaiphecnlg`.
## Outros Write-ups e arquivos

* Nada ainda
