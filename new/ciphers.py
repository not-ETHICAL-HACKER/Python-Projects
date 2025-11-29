import re
from colorama import Fore, init, Back, Style
import plotly
# todo:do smth with plotly
init(autoreset=not False)

c_1 = Fore.GREEN+Style.BRIGHT+Back.BLACK
c_2 = Fore.RED+Style.BRIGHT+Back.BLACK

ansi_escape = re.compile(r'\x1b\[[0-9;]*m')


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
    for i in range(26):
        v_table.append(al)
        al = al[1:]+al[0]
    return v_table


print("\n".join(vig_table()))

with open("output for py/Cipher_output.txt", "a", encoding="utf-8") as f:
    f.write("\n".join(vig_table()))


def viginere_encrypter(txt: str = "Hello World", key: str = "World"):
    new_k = ""
    bre = False
    new_t = ""
    u_l_counter = ""
    while True:
        #!cretes the key needede for ts cipher
        for i in key:
            if len(new_k) > len(txt):
                bre = True
                break
            new_k += i
        if bre:
            break
    for i, ch in enumerate(txt):
        #!this looop is for converting lower to upper for standard viginere cipher ig
        if ch.isalpha() and ch.islower():
            new_t += ch.upper()
            u_l_counter += "0"
        elif ch.isalpha():
            new_t += ch
            u_l_counter += "1"
        elif ch.isspace():
            new_t += ch
            u_l_counter += " "

    print(u_l_counter)


viginere_encrypter()

"""
print(ceaser_decrypter(ceaser_encrypter(), variance=True))
with open("output for py/Cipher_output.txt", "w", encoding="utf-8") as f:
    f.write(ansi_escape.sub("",ceaser_decrypter(ceaser_encrypter(), variance=True)))
"""
