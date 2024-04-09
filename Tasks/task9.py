import re


def main(string):
    while "\n" in string:
        string = string.replace("\n", "")
    result = dict()
    items = list(map(
        lambda x: x.strip() + "FLAG",
        re.findall(r"(?<=<<)(.*?)(?=>>)", string)
    ))
    for item in items:
        key = re.search(r"(?<=decl)(.*?)(?=<==)", item).group().strip()
        value = re.search(r"(?<=<==)(.*?)(?=FLAG)", item).group().strip()
        result[key] = int(value)
    return result


if __name__ == "__main__":
    s = "<: <<decl ingece<==9043 >><< decl maesza <== -8996 >> << decl\natonbe_449 <==-2053>> :>"
    print(main(s))
