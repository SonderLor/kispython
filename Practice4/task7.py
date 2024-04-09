import re


def main(string):
    result = list()
    arrays = re.findall(r"(?<=<sect>)(.*?)(?=</sect>)", string)
    for array in arrays:
        array_name = re.search(r"(?<=q\()\w+(?=\))", array).group()
        lst = re.findall(r"(?<=@')\w+(?=')", array)
        result.append((array_name, list(lst)))
    return result


if __name__ == "__main__":
    s = ("||<sect> data array( @'cebi_815'; @'geso'; @'usla_563') to q(dite_207); </sect>;<sect> data array( @'zaatus_229'; @'ave'; @'enre') to q(raat); </sect>;||")
    print(main(s))
