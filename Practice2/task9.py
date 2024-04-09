def concatenate(words: list[str]) -> str:
    s = ""
    for i in range(len(words) - 1, 0, -1):
        s += words[i] + " "
    s += words[0]
    return s


def frequency(s: str, c: str) -> int:
    result = 0
    for sym in s:
        if sym == c:
            result += 1
    return result


def count_characters(words: str) -> dict[str: int]:
    words = words.lower()
    result = dict()
    for sym in words:
        if sym != " " and sym not in result.keys():
            result[sym] = frequency(words, sym)
    return result


def main() -> None:
    words = ["language!", "programming", "Python", "the", "love", "I"]
    for key, value in count_characters(concatenate(words)).items():
        print(key, value)


if __name__ == "__main__":
    main()
