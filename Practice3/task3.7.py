s = [12, 3250, 31]
print([num for num in s if num % sum(int(digit) for digit in str(num)) == 0])
