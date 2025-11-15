def longest_word_checker(txt: str, l: list) -> bool:
    is_longest = all(len(txt) >= len(word) for word in l)

    if not is_longest:
        print(f"{txt} is not the longest word in {' '.join(l)}")

    l.append(txt)
    return is_longest
def password_cracker(txt:str, time_limt:float)->bool:
    pass
    return True