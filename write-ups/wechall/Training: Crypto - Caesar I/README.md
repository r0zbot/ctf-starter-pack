# We Chall: Training: Crypto - Caesar I
**Categoria:** Training, Crypto
**Pontos:** 1
**Descrição:**

> As on most challenge sites, there are some beginner cryptos, and often you get started with the good old caesar cipher.
>
> I welcome you to the WeChall style of these training challenges :)
>
> Enjoy!
>
> PDA MQEYG XNKSJ BKT FQILO KRAN PDA HWVU ZKC KB YWAOWN WJZ UKQN QJEMQA OKHQPEKJ EO OXWJXWOJJKJW
>
> Disponível em:   <https://www.wechall.net/challenge/training/crypto/caesar/index.php>

## Write-up
Pela descrição da challenge, vemos que o texto está encriptado pela cifra de César.

Como a cifra de César só tem no máximo 25 possibilidades de deslocamento (shift), podemos testar todas os shifts até encontrar o texto correto.

Usando o site <https://www.dcode.fr/caesar-cipher>, temos a opção de testar todas as possibilidades (brute-force attack). E a solução apresentada como mais provável, com shift +22, é
```
THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG OF CAESAR AND YOUR UNIQUE SOLUTION IS SBANBASNNONA
```
É preciso tomar cuidado que o dcode tira os espaços para o brute-force.

**Resposta:** SBANBASNNONA

## Outros Write-ups e arquivos
