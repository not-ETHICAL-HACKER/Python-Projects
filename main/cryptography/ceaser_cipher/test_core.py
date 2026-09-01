from core import encrypt, decrypt


def test_encrypt_basic():
    assert encrypt("abc", 1) == "bcd"


def test_encrypt_wraparound_uppercase():
    assert encrypt("XYZ", 2) == "ZAB"


def test_encrypt_mixed_case_and_symbols():
    assert encrypt("Hello, World!", 5) == "Mjqqt, Btwqi!"


def test_decrypt_basic():
    assert decrypt("bcd", 1) == "abc"


def test_encrypt_then_decrypt_returns_original():
    text = "Python123!"
    shift = 7
    assert decrypt(encrypt(text, shift), shift) == text


def test_negative_shift():
    assert encrypt("abc", -1) == "zab"


def test_large_shift_equivalent():
    assert encrypt("abc", 26) == "abc"

def test_very_large_shift():
    assert encrypt("abc", 67) == "pqr"