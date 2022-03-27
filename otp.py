from secrets import choice
from string import printable

def generate_pad(length:int) -> str:
    pad = ""
    for index in range(length):
        pad_letter =  choice(printable)
        pad += (pad_letter)

    return pad

def encrypt(text:str, pad:str) -> str:
    ciphertext = ""

    for text_character, pad_character in zip(text, pad):
        if text_character not in printable:
            raise ValueError(f"Text value: {text_character} provided is not printable ascii")

        xored_value = ord(text_character) ^ ord(pad_character)

        ciphertext_character = chr(xored_value)

        ciphertext += (ciphertext_character)

    return ciphertext

def decrypt(pad:str, ciphertext:str) -> str:
    plaintext = ""

    for pad_character, ciphertext_number in zip(pad, ciphertext):
        xored_value = ord(pad_character) ^ ord(ciphertext_number)
        plaintext += chr(xored_value)

    # save(plaintext, "plaintext.txt")

    return plaintext

if __name__ == "__main__":
    # The text to encrypt
    text = '''From fairest creatures we desire increase,
That thereby beauty's rose might never die,
But as the riper should by time decease,
His tender heir might bear his memory:
But thou contracted to thine own bright eyes,
Feed'st thy light's flame with self-substantial fuel,
Making a famine where abundance lies,
Thy self thy foe, to thy sweet self too cruel:
Thou that art now the world's fresh ornament,
And only herald to the gaudy spring,
Within thine own bud buriest thy content,
And, tender churl, mak'st waste in niggarding:
Pity the world, or else this glutton be,
To eat the world's due, by the grave and thee.'''

    # Generate a pad the same length as the text
    pad = generate_pad(len(text))
    print(f"The pad is: {pad}")

    # Generate a ciphertext from the pad and plaintext
    ciphertext = encrypt(text, pad)
    print(f"\nThe ciphertext is: {ciphertext}")

    # Decrypt and return result
    plaintext = decrypt(pad, ciphertext)
    print(f"\nThe decrypted plaintext is: {plaintext}")