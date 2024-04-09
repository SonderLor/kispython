import sys


def my_print(*args, sep=' ', end='\n', f=None):
    if f is None:
        output = sep.join(map(str, args)) + end
        sys.stdout.write(output)
    else:
        for line in f.readlines():
            sys.stdout.write(line)


file = open("task2.3.py", "r")
my_print(f=file)
my_print(3, 4, sep="SEP", end=" ")
my_print(3, 4, sep="SEP", end=" ")
file.close()
