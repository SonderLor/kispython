import re


def main(string):
    result = dict()
    arrays = re.findall(r"(?<=<data>)(.*?)(?=<\/data>)", string)
    for array in arrays:
        key = re.search(r"(?<=@\")\w+(?=\")", array).group()
        value = re.search(r"(?<=\=)(.*?)(?= )", array).group()
        result[key] = value
    return result


if __name__ == "__main__":
    s = '[<data>set @"este_583" =5840 </data> <data> set @"usbear" =-2370 </data> <data>set @"arso_10" =-1480 </data><data>set @"vesobi"=2526 </data> ]'
    print(main(s))
