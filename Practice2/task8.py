def concatenate(words: list[str]) -> str:
    s = ""
    for i in range(len(words) - 1, 0, -1):
        s += words[i] + " "
    s += words[0]
    return s


def main() -> None:
    words = ["language!", "programming", "Python", "the", "love", "I"]
    print(concatenate(words))


if __name__ == "__main__":
    main()
