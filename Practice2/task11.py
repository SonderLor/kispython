import timeit
from typing import Callable
from Levenshtein import distance


def levenshtein_distance_recursion(a: str, b: str, i: int = None, j: int = None) -> int:
    if i is None:
        i = len(a) - 1
    if j is None:
        j = len(b) - 1
    if i == 0 or j == 0:
        return max(i, j)
    if a[i - 1] == b[j - 1]:
        return levenshtein_distance_recursion(a, b, i - 1, j - 1)
    return 1 + min(levenshtein_distance_recursion(a, b, i, j - 1),
                   levenshtein_distance_recursion(a, b, i - 1, j),
                   levenshtein_distance_recursion(a, b, i - 1, j - 1))


def levenshtein_distance_cycle(a: str, b: str) -> int:
    len_a = len(a)
    len_b = len(b)
    matrix = [[0] * (len_b + 1) for _ in range(len_a + 1)]
    for i in range(len_a + 1):
        matrix[i][0] = i
    for j in range(len_b + 1):
        matrix[0][j] = j
    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            if a[i - 1] == b[j - 1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j] = min(matrix[i - 1][j] + 1,
                               matrix[i][j - 1] + 1,
                               matrix[i - 1][j - 1] + cost)
    return matrix[len_a][len_b]


def measure_time(algorithm: Callable, strings: list[tuple[str, str]]) -> list[float]:
    times = list()
    for s1, s2 in strings:
        time_taken = timeit.timeit(lambda: algorithm(s1, s2), number=1000)
        times.append(time_taken)
    return times


def main() -> None:
    pairs_of_strings = [("Hello, world!", "Goodbye, world!"),
                        ("Hello, world!", "Bye, world!"),
                        ("I love Python", "I like Python"),
                        ("100101", "100011")]
    rectimes = measure_time(levenshtein_distance_recursion, pairs_of_strings)
    cyctimes = measure_time(levenshtein_distance_cycle, pairs_of_strings)
    сtimes = measure_time(distance, pairs_of_strings)
    print("Моя функция (рекурсия):")
    for words, time in zip(pairs_of_strings, rectimes):
        print(f"{words[0]}\t{words[1]} -> {str(time)}")

    print("\nМоя функция (циклы):")
    for words, time in zip(pairs_of_strings, cyctimes):
        print(f"{words[0]}\t{words[1]} -> {str(time)}")

    print("\nСишная функция:")
    for words, time in zip(pairs_of_strings, сtimes):
        print(f"{words[0]}\t{words[1]} -> {str(time)}")


if __name__ == "__main__":
    main()
