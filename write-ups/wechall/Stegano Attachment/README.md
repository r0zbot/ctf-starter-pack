# We Chall: Stegano Attachment
**Categoria:** Training, Image, Stegano
**Pontos:** 3
**Descrição:**

>Hello challenger,
>
>You got mail and a nice attachment.
>
>Your unique solution which is bound to your session is in there too.
>
>Enjoy!
>
> Disponível em:   <https://www.wechall.net/challenge/training/stegano/attachment/index.php>

## Write-up
Clicando no link, vemos uma imagem no navegador. Em seguida baixamos o arquivo em php.

Uma primeira tentativa é tentar ler o arquivo, usando o comando `cat`:

```
cat attachment.php
```

O resultado são várias informações ilegíveis, porém, encontramos uma frase no final: `solution.txt`.

Assim, sabemos que pode ter um arquivo escondido dentro do php. Para isso, podemos usar o programa `foremost`:
```
foremost attachment.php
```
Com isso, obtemos uma pasta `output`. Nela temos uma pasta `jpg` com a imagem e uma `zip` contendo o arquivo `solution.txt` que estava escondido no php.

Dentro dele está a resposta.

**Resposta:** HISIPGIMCMNI

## Outros Write-ups e arquivos

* Nada ainda
