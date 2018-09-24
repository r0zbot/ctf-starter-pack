bacon_to_letter_26 = {
    'aaaaa':'A', 'aaaab':'B', 'aaaba':'C', 'aaabb':'D', 'aabaa':'E',
    'aabab':'F', 'aabba':'G', 'aabbb':'H', 'abaaa':'I', 'abaab':'J',
    'ababa':'K', 'ababb':'L', 'abbaa':'M', 'abbab':'N', 'abbba':'O',
    'abbbb':'P', 'baaaa':'Q', 'baaab':'R', 'baaba':'S', 'baabb':'T',
    'babaa':'U', 'babab':'V', 'babba':'W', 'babbb':'X', 'bbaaa':'Y',
    'bbaab':'Z'
}

def format(text, a='a', b='b'):
    """Format a steganographic text to a binary sequence"""
    formated_text = ''
    for c in text:
        if not c.isalpha():
            continue
        if c.istitle():
            formated_text += b
        else:
            formated_text += a
    return formated_text

def decode(text, a='a', b='b', bacon_alpha=bacon_to_letter_26):
    """Decode a encrypted Bacon cipher text"""
    cipher = format(text)
    output = ''
    while len(cipher) >= 5:
        token, cipher = cipher[:5], cipher[5:]
        if token in bacon_alpha:
            output += bacon_alpha[token]
        else:
            break
    return output

if __name__ == '__main__':
    input  = input()
    output = decode(input)
    print(output)
