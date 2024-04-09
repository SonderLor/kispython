def levenshtein_distance(a: str, b: str, i: int = None, j: int = None) -> int:
    if i is None:
        i = len(a) - 1
    if j is None:
        j = len(b) - 1
    if i == 0 or j == 0:
        return max(i, j)
    if a[i - 1] == b[j - 1]:
        return levenshtein_distance(a, b, i - 1, j - 1)
    return 1 + min(levenshtein_distance(a, b, i, j - 1),
                   levenshtein_distance(a, b, i - 1, j),
                   levenshtein_distance(a, b, i - 1, j - 1))


def main() -> None:
    pairs_of_strings = [("Hello, world!", "Goodbye, world!"),
                        ("Hello, world!", "Bye, world!"),
                        ("I love Python", "I like Python"),
                        ("100101", "100011")]
    for s1, s2 in pairs_of_strings:
        distance = levenshtein_distance(s1, s2)
        print(f"{s1}\t{s2} -> {distance}")


if __name__ == "__main__":
    main()
