# Cifra de Vigenère

A Cifra de Vigenère é basicamente uma extensão da fórmula da [Cifra de César](caesar-cipher.md).

> Ela tem esse nome em homenagem a Blaise de Vigenère

Essa Cifra consiste basicamente em pegar uma **palavra-chave** e aplicar a cifra de César várias vezes, de acordo com os caracteres da palavra-chave.

Por exemplo, se nós queremos encriptar a mensagem `the cake is a lie` usando a palavra-chave `portal`, primeiro cada caractere da palavra-chave terá um número de rotações equivalente (de acordo com sua posição no alfabeto):

letra    | P | O  | R  | T  | A | L
---|---
rotações | 16| 15 | 18 | 20 | 1 | 12  

Assim, para cada letra da mensagem será rotacionada de acordo com a sequência de rotações acima:

```
mensagem:         T H E  C A K E  I S  A  L I E
chave:            P O R  T A L P  O R  T  A L P
mensagem cifrada: I V V  V A V T  W J  T  L T T
```
## Detectando
(to-do)

## Solucinando
(to-do)

## Exercícios
(to-do)
