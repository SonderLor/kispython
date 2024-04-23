import re
from typing import List, Set
from datetime import datetime


def convert_to_percent(string):
    try:
        percent = float(string) * 100
        return f"{round(percent)}%"
    except ValueError:
        return None


def extract_last_name(full_name):
    pattern = r'^[А-ЯЁа-яё]+\s[А-ЯЁа-яё]\.[А-ЯЁа-яё]\.$'
    if re.match(pattern, full_name):
        last_name = full_name.split()[0]
        return last_name
    else:
        return None


def convert_date(date_string):
    try:
        date = datetime.strptime(date_string, '%y.%m.%d')
        new_date = date.strftime('%d-%m-%y')
        return new_date
    except ValueError:
        return None


def convert_phone_number(phone_string):
    pattern = r'\+7\(\d{3}\)\d{3}-\d{2}-\d{2}'
    if re.match(pattern, phone_string):
        new_phone = re.sub(r'\+7\((\d{3})\)(\d{3})-(\d{2})-(\d{2})',
                           r'\1-\2-\3\4', phone_string)
        return new_phone
    else:
        return None


def transpose(table: List[List[str]]) -> List[List[str]]:
    if not table or not table[0]:
        return []
    transposed_table = [[] for _ in range(len(table[0]))]
    for i in range(len(table)):
        for j in range(len(table[0])):
            transposed_table[j].append(table[i][j])
    return transposed_table


def delete_doubles_in_a_row(table: List[List[str]]) -> List[List[str]]:
    new_table: List[List[str]] = list()
    for index, row in enumerate(table):
        if not (row in new_table or all(elem is None for elem in row)):
            new_table.append(row)
    return new_table


def main(table: List[List[str]]) -> List[List[str]]:
    table = delete_doubles_in_a_row(table)
    table = transpose(table)
    table = delete_doubles_in_a_row(table)
    for row in table:
        for index, elem in enumerate(row):
            if convert_date(elem):
                row[index] = convert_date(elem)
            elif convert_phone_number(elem):
                row[index] = convert_phone_number(elem)
            elif extract_last_name(elem):
                row[index] = extract_last_name(elem)
            elif convert_to_percent(elem):
                row[index] = convert_to_percent(elem)
    return table


if __name__ == "__main__":
    example1: List[List[str]] = [
        ["99.07.01", "Воцоциди А.Н.", None, "+7(938)075-06-23", "0.0", "+7(938)075-06-23"],
        ["99.03.08", "Дегечиди Б.А.", None, "+7(278)472-71-03", "0.3", "+7(278)472-71-03"],
        ["03.07.09", "Луцский Д.У.", None, "+7(070)840-64-18", "0.3", "+7(070)840-64-18"],
        ["99.03.08", "Дегечиди Б.А.", None, "+7(278)472-71-03", "0.3", "+7(278)472-71-03"]
    ]
    example2: List[List[str]] = [
        ["99.06.02", "Викберг О.З.", "+7(087)299-68-10", "0.5", None, "+7(087)299-68-10"],
        ["99.03.01", "Лачов Л.М.", "+7(205)916-24-13", "0.5", None, "+7(205)916-24-13"],
        ["00.10.27", "Гебинук В.Б.", "+7(823)989-83-14", "0.9", None, "+7(823)989-83-14"],
        ["99.03.01", "Лачов Л.М.", "+7(205)916-24-13", "0.5", None, "+7(205)916-24-13"]
    ]
    example2 = main(example2)
    print(*example2, sep="\n")
