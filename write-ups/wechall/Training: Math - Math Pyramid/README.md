# We Chall: Training: Math - Math Pyramid
**Categoria:** Training, Math
**Pontos:** 2
**Descrição:**

>This is the first release of a math challenge.
>
>You have to come up with the shortest solution (9 chars or less) for a geometric function.
>
>And the story goes like:
>
>Pharao momo wants a square-based pyramid, where all the eight edges are of the same length 'a'.
>
>Please support him with a formula to calculate the volume for a given side length.
>
>Your co-workers already drew a sketch how the pyramid looks like from front-view:
>
> ![](pyramid.png)
>
>Example Formula: a^3/3\*sqrt(a\*a)
>
>Notation Hints: sqrt(), a^2, etc.
>
>Enjoy!
>
> Disponível em:   <https://www.wechall.net/challenge/training/math/pyramid/index.php>

## Write-up
Incialmente, o primeiro trabalho do desafio é calcular matematicamente a fórmula do volume dessa pirâmide.

A fórmula do volume de uma pirâmide é

```
(área da base * altura) / 2
```

Como a base é um quadrado, a área é ``` a^2 ```.

A altura pode ser calculada por pitágoras, encontrando ```a / sqrt(2)```.

Logo a fórmula para o volume é

```
a^2 * a / (3 * sqrt(2))
```
Porém, isso não preenche o requisito de menos de 9 caracteres na fórmula.

Assim, podemos simplificá-la fazendo a multiplicação do ```a```, obtendo ``` a ^3```.
E podemos substituir primeiramente ```3 * sqrt(2)``` por ```(18)^0.5``` e finalmente por ```18^.5```.

Assim, obtemos a fórmula final simplificada.

**Resposta:** a^3/18^.5

## Outros Write-ups e arquivos
