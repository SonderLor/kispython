import random


def generate_surname():
    with open("names.txt", "r", encoding="utf-8") as file:
        names = file.readlines()

    name = random.choice(names).strip()

    letters = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЭЮЯ'
    patronymic = random.choice(letters)

    vowels = 'аэиоуяею'
    consonants = 'бвгджзклмнпрстфхцчшщ'
    suffix = ['ский', 'ий', 'ов', 'ев', 'енко', 'ко', 'ян', 'ин', 'слав', '']

    surname = ''
    surname += random.choice(consonants).upper()
    surname += random.choice(vowels)
    surname += random.choice(consonants)
    if random.randint(0, 1):
        surname += random.choice(vowels)
        surname += random.choice(consonants)
    surname += random.choice(suffix)

    return f'{name} {patronymic}. {surname}'


if __name__ == "__main__":
    for _ in range(15):
        print(generate_surname())
