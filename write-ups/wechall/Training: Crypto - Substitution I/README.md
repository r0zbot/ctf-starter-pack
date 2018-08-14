# We Chall: Training: Crypto - Substitution I

**Categoria:** Training, Crypto
**Pontos:** 2
**Descrição:**

> Oh dear, I guess you have cracked the two caesar cryptos...
>
> This one is more difficult. Although a simple substitution is easily cracked...
>
> Again the characters are limited to A-Z... But I think I can come up with a 256 version again.
>
>Enjoy!
>
> XH KVT EDRJYVKH YLU HLN GEM ZTEU KVJP RH BZJTMU J ER JRFZTPPTU WTZH QTDD ULMT HLNZ PLDNKJLM CTH JP JZPULVPPJTVJ KVJP DJKKDT GVEDDTMYT QEP MLK KLL VEZU QEP JK
>
> Disponível em:   <https://www.wechall.net/challenge/training/crypto/simplesub1/index.php>

## Write-up
Pelo enunciado, sabemos que a mensagem foi cifrada pelo método de simples substituição.

Usar força bruta para encontrar a resposta é inviável, por isso devemos usar algum método de cripto análise que faça a análise das frequências das letras. Um jeito prático seria usar a ferramenta implementada nesta página: https://www.guballa.de/substitution-solver.

Assim, regulando o programa para o inglês e clicando para quebrar a cifra encontramos

`
BY THE ALMIGHTY GOD YOU CAN READ THIS MY FRIEND I AM IMPRESSED VERY WELL DONE YOUR SOLUTION KEY IS IRSDOHSSIEHI THIS LITTLE CHALLENGE WAS NOT TOO HARD WAS IT
`

**Resposta:** `IRSDOHSSIEHI`

## Outros Write-ups e arquivos

* Nada ainda
