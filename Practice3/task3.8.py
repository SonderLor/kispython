import itertools


s = 'ABBCCCDEFAAA'
print([(sym, len(list(repeats))) for sym, repeats in itertools.groupby(s)])
