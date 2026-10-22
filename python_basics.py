def count_vowels(s):
    count = 0
    for letter in s:
        if any(letter.lower() == el for el in "aeiou"):
            count += 1
    return count


def has_unique_characters(s):
    d = {}
    for ch in s:
        if ch not in d:
            d[ch] = 1
        else:
            return False
    return True


def count_one_bits(num):
    b = bin(num)[2:]
    count = 0
    print(b)
    for el in str(b):
        if el == '1':
            count += 1
    return count


def multiplicative_persistence(num, count=0):
    multipliers = []
    while num > 0:
        multipliers.append(num % 10)
        num //= 10
    mp = 1
    for el in multipliers:
        mp *= el
    count += 1
    if mp % 10 == mp:
        return count
    else:
        return multiplicative_persistence(mp, count)


def mse(x, y):
    return sum((x[i] - y[i]) ** 2 for i in range(len(x))) / len(x)


def prime_factorization(num):
    multipliers = []
    el = 2
    while num != 1:
        if num % el == 0:
            multipliers.append(el)
            num //= el
        else:
            el += 1
    d = {}
    for n in multipliers:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
    result = ""
    for key in d:
        if d[key] != 1:
            result += f"({key}**{d[key]})"
        else:
            result += f"({key})"
    return result


def pyramid(n):
    num = 1
    sum = 0
    while sum < n:
        sum += num ** 2
        num += 1
    if sum == n:
        return num - 1
    else:
        return "It is impossible"


def is_balanced_number(num):
    sNum = str(num)
    length = len(sNum)
    if length % 2 == 0:
        halfLength = length // 2 - 1
    else:
        halfLength = (length - 1) // 2
    left = sNum[:halfLength]
    right = sNum[-halfLength:]
    return (sum((int(n)) for n in left)) == (sum((int(n)) for n in right))

