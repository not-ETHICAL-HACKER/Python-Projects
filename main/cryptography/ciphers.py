import re
from colorama import Fore, init, Back, Style
import plotly
# todo:do smth with plotly
init(autoreset=True)

c_1 = Fore.GREEN+Style.BRIGHT+Back.BLACK
c_2 = Fore.RED+Style.BRIGHT+Back.BLACK

ansi_escape = re.compile(r'\x1b\[[0-9;]*m')


class UnEncryptableError(Exception):
    pass


def kaiser(char: str, k: int) -> str:
    base = 32
    limit = 126
    rng = limit - base + 1
    code = ord(char)
    if code < base or code > limit:
        return char
    new_code = base + ((code - base + k) % rng)
    return chr(new_code)


def ceaser_encrypter(txt: str = "Hello World", key: int = 3) -> str:
    enc = ""
    for i in txt:
        enc += kaiser(i, key)
    return enc


def ceaser_decrypter(txt: str = "Khoor#Zruog", key: int = 3, variance: bool = False) -> str:
    dec = ""
    if not variance:
        return c_1+"".join(kaiser(i, -key) for i in txt)
    else:
        l: list[str] = []
        for i in range(-26, 27):
            if i == 0:
                continue
            dec = "".join(kaiser(ch, -i) for ch in txt)
            l.append(f"{c_2}{i:2d}{Fore.GREEN+Style.BRIGHT} -> {c_1}{dec}")
        return "\n".join(l)

    """
    The function includes a Caesar encryption and decryption algorithm with the option to display
    multiple decryption attempts with different keys.
    
    :param txt: The `txt` parameter in the `ceaser_encrypter` and `ceaser_decrypter` functions
    represents the text that you want to encrypt or decrypt using the Caesar cipher algorithm. In the
    provided code snippet, the default value for `txt` is set to "Hello World" for encryption and,
    defaults to Hello World
    :type txt: str (optional)
    :param key: The `key` parameter in the `ceaser_encrypter` and `ceaser_decrypter` functions
    represents the shift value used in the Caesar cipher algorithm. It determines how many positions
    each character in the input text should be shifted to encrypt or decrypt the text. In the provided
    code snippet, the, defaults to 3
    :type key: int (optional)
    :return: The code defines a Caesar encryption and decryption functions. The `ceaser_encrypter`
    function takes a text string and a key, and returns the encrypted text using the Caesar cipher. The
    `ceaser_decrypter` function takes an encrypted text string, a key, and a variance flag. If the
    variance flag is False, it returns the decrypted text using the Caesar cipher. If the variance flag
    is
    """


def vig_table() -> list[str]:
    v_table = []
    al = "".join(list(chr(k) for k in range(65, 91)))
    for _ in range(26):
        v_table.append(al)
        al = al[1:]+al[0]
    return v_table


"""
print("\n".join(vig_table()))

with open("output for py/Cipher_output.txt", "a", encoding="utf-8") as f:
    f.write("\n".join(vig_table()))
"""


def viginere_encrypter(txt: str = "rgtfvdsuybciunxddfieniggerfbdifdyfbdf", key: str = "World"):
    forbid=set(chr(cha) for cha in range(33,65))
    if  any(ch in forbid for ch in txt) or any(ch in forbid for ch in key):
        raise UnEncryptableError("The Text Is UnEncryptable.")
    new_k = ""
    new_t = ""
    u_l_counter = ""
    enc = ""
    v_tab = vig_table()
    for i, ch in enumerate(txt):
        #!this looop is for converting lower to upper for standard viginere cipher ig
        if ch.isalpha() and ch.islower():
            new_t += ch.upper()
            u_l_counter += "0"
        elif ch.isalpha():
            new_t += ch
            u_l_counter += "1"
        else:
            new_t+=ch
            u_l_counter+=" "
        # Build repeated key (uppercase)
    new_k = (key * ((len(txt) // len(key)) + 1))[:len(txt)]
    new_k = new_k.upper()
    enc = ""
    ki = 0  # key index
    for t_char in new_t:
        if t_char == " ":       # or t_char.isspace()
            enc += " "
            continue

        # apply key only to letters
        k_char = new_k[ki]   
        ki += 1                 # advance key ONLY HERE
        row = ord(k_char) - 65
        col = ord(t_char) - 65
        enc += v_tab[row][col]

    print("Encrypted:", enc)
    print("Case mask:", u_l_counter)
    print(f"Key : {key}")

def vigenere_decrypt(ciphertext: str, key: str) -> str:
    plaintext = ""
    key_index = 0
    key = key.lower()

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')

            # decrypt
            base = ord('A') if char.isupper() else ord('a')
            p = chr((ord(char) - base - shift) % 26 + base)

            plaintext += p
            key_index += 1
        else:
            # non letters unchanged
            plaintext += char

    return plaintext

def shift_encrypter(txt:str="Hello world",key:int=2)->str:
    enc=""
    for i in txt:
        enc += chr((ord(i) << key) & 0x10FFFF)
    print(enc)
    return enc
def shift_decrypter(txt:str,key:int=2)->str:
    dec=""
    for i in txt:
        dec+=chr(int(ord(i)>>key))
    print(dec)
    return dec

def xor_encrypt(text: str, key: int) -> str:
    return "".join(chr(ord(c) ^ key) for c in text)

def xor_decrypt(text: str, key: int) -> str:
    return "".join(chr(ord(c) ^ key) for c in text)
print(xor_encrypt("Hello World",2))
"""
print(ceaser_decrypter(ceaser_encrypter(), variance=True))
with open("output for py/Cipher_output.txt", "w", encoding="utf-8") as f:
    f.write(ansi_escape.sub("",ceaser_decrypter(ceaser_encrypter(), variance=True)))
"""
