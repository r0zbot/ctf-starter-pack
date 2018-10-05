# picoCTF - 2018: LoadSomeBits

**Categoria:** Forensics
**Pontos:** 550
**Descrição:**

> Can you find the flag encoded inside this image? You can also find the file in /problems/loadsomebits_1_5ccf71e5726692c713405bb17da5cb37 on the shell server.
>
> [Imagem](pico2018-special-logo.bmp)
>
> Hints:
>
> Look through the Least Significant Bits for the image
>
> If you interpret a binary sequence (seq) as ascii and then try interpreting the same binary sequence from an offset of 1 (seq[1:]) as ascii do you get something similar or completely different?

## Write-up
Pelo enunciado, vemos que a flag está escondida na imagem por meio da técnica esteganográfica LSB (_Least Significant Bits_). Assim, podemos criar um programa em Python para extrair essa informação.

**Fonte:** [lsb_decode.py](lsb_decode.py)
```python
from bitstring import BitStream, BitArray

file = "pico2018-special-logo.bmp"
header = 14*8

b = BitArray(bytes=open(file, 'rb').read())
nb = b.bin[header:]

bin_char = ''
count = 0
while len(nb) > 0:
    byte, nb = nb[:8], nb[8:]
    bin_char += byte[-1]
    count += 1
    if len(bin_char) == 8:
        print(chr(int(bin_char, 2)), end='')
        bin_char = ''
    if count > 2000:
        break
```

**Resposta:** `picoCTF{st0r3d_iN_tH3_l345t_s1gn1f1c4nT_b1t5_882756901}`.
## Outros Write-ups e arquivos

* Nada ainda
