# We Chall: hi

**Categoria:** Math
**Pontos:** 3
**Descrição:**

>Hi, imagine this situation.
>
>There is an IRC channel #wechall on irc.idlemonkeys.net.
>
>The server sends the messages to all people in the channel, also back to the sender himself.
>
>When every minute one person joins and says hi,
>
>how many "hi" messages were totally sent for this channel after 0xfffbadc0ded minutes ?
>
>No one ever leaves the channel, so there are 0xfffbadc0ded people at the end ;)
>
>
>
>Further explanation for 3 minutes:
>
>the channel is empty and there have been sent 0 messages 1st person joins, sends hi, the server sends hi back to 1 persons.
>
>2nd person joins, sends hi, the server sends hi back to 2 persons.
>
>3rd person joins, sends hi, the server sends hi back to 3 persons.
>
>
>
>Minute 1: 2 messages sent
>
>Minute 2: 3 messages sent
>
>Minute 3: 4 messages sent
>
>Adding these up means for 3 minutes are 9 messages sent.
>
>
>Conversion Notes: 0xfffbadc0ded is hexadecimal which converts to 17.591.026.060.781 (Thats around 20 trillion minutes).Please submit your solution in the decimal system.
>
> Disponível em: https://www.wechall.net/challenge/hi/index.php

## Write-up
Esse é basicamente um problema de matemática. Pelo enunciado, conseguimos concluir que no minuto `n` temos `n+1` mensagens sendo enviadas e que até o minuto `n` foram enviados um total de `((n+1) + 2) * n/2` mensagens, pois o envio de mensagens cresce numa progressão aritmética.

Dessa forma, queremos encontrar o valor da soma `((n+1) + 2) * n/2` para o minuto `n = 17.591.026.060.781`. Para fazer esse cálculo, podemos usar um interpretador python to terminal

```
$> python3
>>> (17_591_026_060_782 + 2) * 17_591_026_060_781 // 2
```
Assim, encontramos a resposta.

**Resposta:** `154722098935564539692256152`.
## Outros Write-ups e arquivos

* Nada ainda
