def capitalize_words(s: str) -> str:
    return " ".join(word.capitalize() for word in s.split(" "))


def utf8_byte_length(s: str) -> int:
    return len(s.encode("utf-8"))


def caesar_shift(s: str, k: int) -> str:
    result = []
    for ch in s:
        if "a" <= ch <= "z":
            result.append(chr((ord(ch) - ord("a") + k) % 26 + ord("a")))
        elif "A" <= ch <= "Z":
            result.append(chr((ord(ch) - ord("A") + k) % 26 + ord("A")))
        else:
            result.append(ch)
    return "".join(result)
